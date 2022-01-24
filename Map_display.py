from pprint import pprint
from random import sample

from Car import Car
from Menu import menu
from Road import Road
from Save import Save


def map_display(screen, size: tuple[int, int], save: Save, road: Road = None):
    import pygame

    from Button import Button
    from Mark import Mark, Locality

    from Image import Image
    from Road import Map, Road, Text
    from random import choice
    from Choosing_car import choosing_car
    import pickle

    from Starter import Starter

    if road is not None:
        way = road.way
    else:
        way = []

    # создадим группу, содержащую все спрайты
    marks_sprites = pygame.sprite.Group()
    map_sprites = pygame.sprite.Group()
    buttons_sprites = pygame.sprite.Group()

    image_map = Image(Map.save_path.format('map1', 'map.jpg'))
    maps = Map(image_map, map_sprites)

    # CONST
    k_image_width = size[0] / maps.image.get_width()
    k_image_height = size[1] / maps.image.get_height()
    R_CIRCLE = 350 * k_image_height
    Y_TEXT_MAX = 350 * k_image_height * 0.8
    X_CIRCLE = size[0] - R_CIRCLE * 0.5
    Y_CIRCLE = 0
    TEXT_Height = int(60 * k_image_height)
    X_TEXT = int(size[0] - (size[0] - X_CIRCLE) - R_CIRCLE * 0.7)
    X_BUTTON_GO = int(0.72 * size[0])
    Y_BUTTON_GO = int(0.93 * size[1])
    X_BUTTON_EXIT = int(0.02 * size[0])
    Y_BUTTON_EXIT = Y_BUTTON_GO
    COUNT_MARK = 5

    maps.deafult_image.transform(size[0], size[1])
    maps.image = maps.deafult_image.image
    maps.load('map1')

    if len(save.road_and_car) == 0:
        start_point = maps.start
    else:
        start_point = [i for i in save.road_and_car][-1].finish

    points = maps.dct_points

    # print(points)

    marks = []
    class_cars = [Car.get_class_car(path=i) for i in save.specifications.name_cars]
    tupls = [i for i in points if type(points[i]) is Locality and start_point != points[i]]
    lst = sample(tupls, COUNT_MARK)
    for i in range(COUNT_MARK):
            mark = Mark(
                button=Button(Image("data/Метка.png"), k_image_width, k_image_height, marks_sprites),
                class_car=choice(class_cars))
            mark.centering(points[lst[i]].get_coords(k_image_width, k_image_height))
            marks.append(mark)

    texts = dict()
    texts['distance'] = Text("Дистанция: ", height=TEXT_Height, x=X_TEXT)
    texts['class'] = Text("Класс: ", height=TEXT_Height, x=X_TEXT)
    texts['money'] = Text("Монеты: ", height=TEXT_Height, x=X_TEXT)

    y_text = (Y_TEXT_MAX - ((len(texts) + 1) * TEXT_Height)) / (len(texts) + 1)
    for i in texts:
        texts[i].y = y_text
        y_text += TEXT_Height + (Y_TEXT_MAX - ((len(texts) + 1) * TEXT_Height)) / (len(texts) + 1)

    del y_text

    buttons = []

    button_go = Button(Image("data/Кнопка.png"), 1, 1)
    k = size[1] * 0.06 / button_go.rect.height
    button_go = Button(Image("data/Кнопка.png"), k, k, buttons_sprites)
    button_go.rect.x = X_BUTTON_GO
    button_go.rect.y = Y_BUTTON_GO
    button_go.set_text("К выбору машины")
    buttons.append(button_go)

    button_exit = Button(Image("data/Кнопка.png"), 1, 1)
    k = size[1] * 0.06 / button_exit.rect.height
    button_exit = Button(Image("data/Кнопка.png"), k, k, buttons_sprites)
    button_exit.rect.x = X_BUTTON_EXIT
    button_exit.rect.y = Y_BUTTON_EXIT
    button_exit.set_text("Сохранить и выйти")
    buttons.append(button_exit)

    del k

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for mark in marks:
                    if mark.button.rect.collidepoint(event.pos):
                        mark.button.change_picture(Image("data/Метка активная.png"), k_image_width,
                                                   k_image_height)
                        mark.centering()
                    else:
                        mark.button.set_deafult()
                        mark.centering()
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.change_picture(Image("data/Кнопка светлая.png"),
                                              button.deafult_k_image_width,
                                              button.deafult_k_image_height)
                    else:
                        button.set_deafult()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_go.rect.collidepoint(event.pos):
                    if road is not None:
                        road.money = int(texts['money'].value[0])
                        starter = Starter(choosing_car, screen, size, save, road)
                        road.specifications = maps.specifications
                        road.money = int(texts['money'].value[0])
                        pickle.dump((save, road), open('Tools/stat_save_road_car.txt', 'wb+'))
                        return starter
                if button_exit.rect.collidepoint(event.pos):
                    save.save()
                    starter = Starter(menu, screen, size)
                    return starter
                for mark in marks:
                    if mark.button.rect.collidepoint(event.pos):
                        finish = mark.get_coords(1 / k_image_width, 1 / k_image_height)
                        finish = round(finish[0]), round(finish[1])
                        road = Road(start_point, points[finish])
                        way = road.find_way(maps.conversion_graph)
                        distance = road.get_distance()
                        texts['distance'].value = [
                            str(round(distance / maps.specifications.PX_KM, 2)), ' км']
                        texts['money'].value = [
                            str(round(
                                float(texts['distance'].value[0]) * maps.specifications.MONEY_KM)),
                            ' шт']
                        texts['class'].value = [mark.class_car.name]
                        road.finish.class_car = mark.class_car
                        pprint(way)
                        break
        screen.fill(pygame.Color((0, 0, 0)))
        map_sprites.draw(screen)
        pygame.draw.circle(screen, (0, 0, 0), (X_CIRCLE, Y_CIRCLE), R_CIRCLE)
        if len(way) != 0:
            coords_last = (way[0].x * k_image_width, way[0].y * k_image_height)
            for i in range(1, len(way)):
                coords = (way[i].x * k_image_width, way[i].y * k_image_height)
                pygame.draw.line(screen, (0, 0, 0), coords_last, coords,
                                 max(1, int(7 * k_image_width)))
                coords_last = coords
        marks_sprites.draw(screen)
        for i in texts:
            texts[i].render(screen)
        buttons_sprites.draw(screen)
        for button in buttons:
            button.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
