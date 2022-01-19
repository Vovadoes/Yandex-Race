import os

import pygame

from Button import Button
from Car import Car
from Image import Image
from Road import Road
from Save import Save
from MAIN_WINDOW import main_game
from Starter import Starter


def choosing_car(screen, size: tuple[int, int], save: Save, road: Road):
    arrows_sprites = pygame.sprite.Group()
    background_sprites = pygame.sprite.Group()

    background = Image('data/Фон выбора машины.png')

    # CONST
    k_image_width = size[0] / background.image.get_width()
    k_image_height = size[1] / background.image.get_height()
    k_image_standart = min(k_image_width, k_image_height)

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(background_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background.image, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    cars = []
    for i in os.listdir(os.path.join(Car.path_save)):
        car = Car().load(name=i)
        car.basic_image = Button(car.basic_image.deafult_image,
                                 size[1] * 0.8 / car.basic_image.rect.height,
                                 size[1] * 0.8 / car.basic_image.rect.height)
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

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cars[index_car].basic_image.rect.collidepoint(event.pos):
                    starter = Starter(main_game, screen, size, save, road, cars[index_car])
                    return starter
                if button_left.rect.collidepoint(event.pos):
                    index_car = (index_car - 1) % len(cars)
                    print("button_left")
                if button_right.rect.collidepoint(event.pos):
                    index_car = (index_car + 1) % len(cars)
                    print("button_right")
        screen.fill(pygame.Color((0, 0, 0)))
        background_sprites.draw(screen)
        screen.blit(cars[index_car].basic_image.image, cars[index_car].basic_image.rect)
        arrows_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
