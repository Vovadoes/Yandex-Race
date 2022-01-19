import pickle

import pygame

from Button import Button
from Mark import Mark, Locality
from Save import Save
from Car import classes_car
from Image import Image
from Road import Map, Road, Text
from random import choice
from Choosing_car import choosing_car
import pickle

from Starter import Starter


def map_display(screen, size: tuple[int, int], save: Save):
    # создадим группу, содержащую все спрайты
    marks_sprites = pygame.sprite.Group()
    map_sprites = pygame.sprite.Group()

    image_map = Image(Map.save_path.format('map1', 'map.jpg'))
    maps = Map(image_map, map_sprites)

    # CONST
    k_image_width = size[0] / maps.image.get_width()
    k_image_height = size[1] / maps.image.get_height()
    maps.PX_KM = 10  # Сколько пикселей в 1ом километре
    maps.MONEY_KM = 10  # колиство монет за 1 км
    R_CIRCLE = 350 * k_image_height
    Y_TEXT_MAX = 350 * k_image_height * 0.8
    X_CIRCLE = size[0] - R_CIRCLE * 0.5
    Y_CIRCLE = 0
    TEXT_Height = int(60 * k_image_height)
    X_TEXT = int(size[0] - (size[0] - X_CIRCLE) - R_CIRCLE * 0.7)

    maps.deafult_image.transform(size[0], size[1])
    maps.image = maps.deafult_image.image
    maps.load('map1')

    if len(save.road_and_car) == 0:
        start_point = maps.start
    else:
        start_point = save.road_and_car[-1].finish

    points = maps.dct_points

    way = []
    print(points)

    global classes_car
    marks = []
    classes_car = classes_car[:save.info['max_level_car'] + 1:]
    for tupl in points:
        if type(points[tupl]) is Locality:
            mark = Mark(
                button=Button(Image("data/Метка.png"), k_image_width, k_image_height, marks_sprites),
                class_car=choice(classes_car))
            mark.centering(points[tupl].get_coords(k_image_width, k_image_height))
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

    fps = 30
    running = True
    clock = pygame.time.Clock()

    road = None

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for mark in marks:
                    if mark.button.rect.collidepoint(event.pos):
                        finish = mark.get_coords(1 / k_image_width, 1 / k_image_height)
                        finish = round(finish[0]), round(finish[1])
                        if road is not None:
                            road.money = int(texts['money'].value[0])
                            if way[-1] == points[finish]:
                                starter = Starter(choosing_car, screen, size, save, road)
                                pickle.dump((save, road),
                                            open('Tools/stat_save_road_car.txt', 'wb+'))
                                return starter
                        road = Road(start_point, points[finish])
                        way = road.find_way(maps.conversion_graph)
                        distance = road.get_distance()
                        texts['distance'].value = [str(int(distance / maps.PX_KM)), ' км']
                        texts['money'].value = [
                            str(int(int(texts['distance'].value[0]) * maps.MONEY_KM)),
                            ' шт']
                        texts['class'].value = [mark.class_car.name]
                        print(way)
                        break
        screen.fill(pygame.Color((0, 0, 0)))
        map_sprites.draw(screen)
        pygame.draw.circle(screen, (0, 0, 0), (X_CIRCLE, Y_CIRCLE),
                           R_CIRCLE)
        if len(way) != 0:
            coords_last = (way[0].x * k_image_width, way[0].y * k_image_height)
            for i in range(1, len(way)):
                coords = (way[i].x * k_image_width, way[i].y * k_image_height)
                pygame.draw.line(screen, (0, 0, 0), coords_last, coords,
                                 max(1, int(7 * k_image_width)))
                coords_last = coords
        marks_sprites.draw(screen)
        # for mark in marks:
        #     mark.button.render_text(screen)
        for i in texts:
            texts[i].render(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
