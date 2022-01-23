import pygame
import os
from Car import Car
from Save import Save
from Road import Road, Text
from Button import Button
from Image import Image


def choosing_car(screen, size: tuple[int, int], save: Save, road: Road):
    from MAIN_WINDOW import main_game
    from Starter import Starter

    arrows_sprites = pygame.sprite.Group()
    background_sprites = pygame.sprite.Group()
    buttons_sprites = pygame.sprite.Group()
    clok_sprites = pygame.sprite.Group()

    background = Image('data/Фон выбора машины.png')

    # CONST
    k_image_width = size[0] / background.image.get_width()
    k_image_height = size[1] / background.image.get_height()
    k_image_standart = min(k_image_width, k_image_height)
    TEXT_Height = int(6 * k_image_standart)
    X_TEXT = int(0.02 * size[0])
    Y_BLOCK_BEGIN_TEXT = int(0.54 * size[1])
    Y_BLOCK_END_TEXT = int(0.97 * size[1])
    X_BUTTON = int(0.65 * size[0])
    Y_BUTTON = int(0.9 * size[1])

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(background_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background.image, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    cars = []
    for i in os.listdir(os.path.join(Car.path_save)):
        car = Car().load(path=i)
        k = min(size[1] * 0.8 / car.basic_image.rect.height, size[0] * 0.8 / car.basic_image.rect.width)
        car.basic_image = Button(car.basic_image.deafult_image,
                                 k,
                                 k)
        car.basic_image.rect.x = (size[0] - car.basic_image.rect.width) // 2
        car.basic_image.rect.y = (size[1] - car.basic_image.rect.height) // 2
        cars.append(car)

    index_car = 0

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

    del k

    texts = dict()
    for i in Car.specifications:
        texts[i] = Text(f"{i}: ", height=TEXT_Height, x=X_TEXT)
        texts[i].value = [Car.specifications[i]]

    print(texts)

    d_y_text = (Y_BLOCK_END_TEXT - Y_BLOCK_BEGIN_TEXT - (len(texts) * TEXT_Height)) / (
            len(texts) + 1)
    y_text = Y_BLOCK_BEGIN_TEXT + d_y_text
    for i in texts:
        texts[i].y = y_text
        y_text += TEXT_Height + d_y_text

    del d_y_text
    del y_text

    button = Button(Image("data/Кнопка.png"), 1, 1)
    k = size[1] * 0.08 / button.rect.height
    button = Button(Image("data/Кнопка.png"), k, k, buttons_sprites)
    button.rect.x = X_BUTTON
    button.rect.y = Y_BUTTON
    button.set_text("Поехали)")

    lock_button = Button(Image("data/lock.png"), 1, 1)
    k = size[1] * 0.08 / lock_button.rect.height
    lock_button = Button(Image("data/lock.png"), k, k, clok_sprites)
    lock_button.rect.x = X_BUTTON
    lock_button.rect.y = Y_BUTTON
    lock_button.set_text("Поехали)")


    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if button.rect.collidepoint(event.pos):
                    button.change_picture(Image("data/Кнопка светлая.png"),
                                          button.deafult_k_image_width,
                                          button.deafult_k_image_height)
                else:
                    button.set_deafult()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    starter = Starter(main_game, screen, size, save, road, cars[index_car])
                    return starter
                if button_left.rect.collidepoint(event.pos) or button_right.rect.collidepoint(event.pos):
                    if button_left.rect.collidepoint(event.pos):
                        index_car = (index_car - 1) % len(cars)
                        print("button_left")
                    else:
                        index_car = (index_car + 1) % len(cars)
                        print("button_right")
        screen.fill(pygame.Color((0, 0, 0)))
        background_sprites.draw(screen)
        screen.blit(cars[index_car].basic_image.image, cars[index_car].basic_image.rect)
        arrows_sprites.draw(screen)
        for i in texts:
            texts[i].render(screen)
        buttons_sprites.draw(screen)
        button.render_text(screen)
        clok_sprites.draw(screen)
        print(cars[index_car].info["name"], save.specifications.name_cars)
        clock.tick(fps)
        pygame.display.flip()
    return None
