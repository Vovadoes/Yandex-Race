import os
import datetime

import pygame

from Car import Car
from Image import Image
from Road import Text
from Save import Save
from Starter import Starter


def saves_dislpay(screen, size):
    from Menu import menu
    from Button import Button

    background_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    buttons_sprites = pygame.sprite.Group()
    arrows_sprites = pygame.sprite.Group()

    background = Image('data/Фон выбора машины.png')

    # CONST
    k_image_width = size[0] / background.image.get_width()
    k_image_height = size[1] / background.image.get_height()
    k_image_standart = min(k_image_width, k_image_height)
    X_BUTTON_EXIT = int(0.02 * size[0])
    Y_BUTTON_EXIT = int(0.9 * size[1])
    TEXT_Height = int(4 * k_image_standart)
    X_TEXT_BEGIN = int(0.20 * size[0])
    X_TEXT_END = int(0.38 * size[0])
    Y_BLOCK_BEGIN_TEXT = 0
    Y_BLOCK_END_TEXT = size[1] - X_BUTTON_EXIT

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(background_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background.image, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    buttons = []

    button_exit = Button(Image("data/Кнопка.png"), 1, 1)
    k = size[1] * 0.07 / button_exit.rect.height
    button_exit = Button(Image("data/Кнопка.png"), k, k, buttons_sprites)
    button_exit.rect.x = X_BUTTON_EXIT
    button_exit.rect.y = Y_BUTTON_EXIT
    button_exit.set_text("Назад")
    button_exit.starter = Starter(menu, screen, size)
    buttons.append(button_exit)

    table = Button(Image("data/table.png"), 1, 1)
    k = min(size[1] / table.rect.height,
            size[0] / table.rect.width)
    table = Button(Image("data/table.png"), k, k, background_sprites)
    table.rect.x = (size[0] - table.rect.width) // 2
    table.rect.y = (size[1] - table.rect.height) // 2

    button_left = Button(Image(r"data/Стрелка влево.png"), 1, 1, x=0)
    button_right = Button(Image(r"data/Стрелка вправо.png"), 1, 1, x=0)

    k = size[1] * 0.1 / button_right.rect.height
    button_right = Button(button_right.last_image, k, k, arrows_sprites)
    button_right.rect.y = (size[1] - button_right.rect.height) // 2
    button_right.rect.x = size[0] - button_left.rect.width - 10

    k = size[1] * 0.1 / button_left.rect.height
    button_left = Button(button_left.last_image, k, k, arrows_sprites)
    button_left.rect.y = (size[1] - button_left.rect.height) // 2
    button_left.rect.x = 10

    cars = []
    for i in os.listdir(os.path.join(Car.path_save)):
        car = Car().load(path=i)
        cars.append(car)

    texts = {}
    saves = Save.set_all_saves()
    index_save = 0
    print(saves)
    recalculate_car = True
    if len(saves) == 0:
        recalculate_car = False
        texts['error'] = Text(f"Сохранений нет", height=TEXT_Height, x=X_TEXT_BEGIN)
        texts['error'].value = ['']
    else:
        texts['name'] = Text(f"Имя сохранения: ", height=TEXT_Height, x=X_TEXT_BEGIN)
        texts['cars'] = Text(f"Количество машин: ", height=TEXT_Height, x=X_TEXT_BEGIN)
        texts['roads'] = Text(f"Количество проездок: ", height=TEXT_Height, x=X_TEXT_BEGIN)
        texts['final_roads'] = Text(f"Количество завершенных проездок: ", height=TEXT_Height, x=X_TEXT_BEGIN)
        texts['date'] = Text(f"Дата сохранения: ", height=TEXT_Height, x=X_TEXT_BEGIN)
        saves.sort(key=lambda i: i['date'], reverse=True)

    d_y_text = (Y_BLOCK_END_TEXT - Y_BLOCK_BEGIN_TEXT - (len(texts) * TEXT_Height)) / (
            len(texts) + 1)
    y_text = Y_BLOCK_BEGIN_TEXT + d_y_text
    for i in texts:
        texts[i].y = y_text
        y_text += TEXT_Height + d_y_text


    fps = 60
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.change_picture(Image("data/Кнопка светлая.png"),
                                              button.deafult_k_image_width,
                                              button.deafult_k_image_height)
                    else:
                        button.set_deafult()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.starter is not None:
                            return button.starter
                if button_left.rect.collidepoint(event.pos) or button_right.rect.collidepoint(
                        event.pos):
                    if len(saves) != 0:
                        if button_left.rect.collidepoint(event.pos):
                            index_save = (index_save - 1) % len(saves)
                            # print("button_left")
                        else:
                            index_save = (index_save + 1) % len(saves)
                            # print("button_right")
                        recalculate_car = True
        if recalculate_car:
            save = Save().load(path=Save.get_path(saves[index_save]["name"]))
            print(save.specifications.name_cars)
            texts['name'].value = [saves[index_save]["name"]]
            texts['cars'].value = [len(save.specifications.name_cars), ' из ', len(cars)]
            texts['roads'].value = [len(save.road_and_car)]
            texts['final_roads'].value = [len(list(filter(lambda j: j.complete_trip, [i for i in save.road_and_car])))]
            texts['date'].value = [saves[index_save]["date"]]
            a = datetime.datetime(2022, 1, 26, 22, 18, 33, 253000)
            recalculate_car = False


        screen.fill(pygame.Color((0, 0, 0)))
        background_sprites.draw(screen)
        all_sprites.draw(screen)
        arrows_sprites.draw(screen)
        buttons_sprites.draw(screen)
        for i in texts:
            texts[i].render(screen)
        for i in buttons:
            i.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None