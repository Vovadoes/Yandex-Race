import pygame
import os
import sys
from pygame.locals import *


def load_image(name, colorkey=None):
    fullname = os.path.join('picturs', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Yandex_Race')
    size = width, height = 400, 799
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60  # пикселей в секунду
    clock = pygame.time.Clock()

    # первая дорога
    all_sprites = pygame.sprite.Group()
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = load_image("3_polos.png")
    sprite1.rect = sprite1.image.get_rect()
    all_sprites.add(sprite1)
    sprite1.rect.x = 0
    sprite1.rect.y = 0
    # вторая дорога
    sprite2 = pygame.sprite.Sprite()
    sprite2.image = load_image("3_polos.png")
    sprite2.rect = sprite2.image.get_rect()
    all_sprites.add(sprite2)
    sprite2.rect.x = 0
    sprite2.rect.y = -798
    # машинка
    car = pygame.sprite.Sprite()
    car.image = load_image("real_car.png")
    car.rect = car.image.get_rect()
    all_sprites.add(car)
    car.rect.x = 50
    car.rect.y = 500

    speed = 3
    directions = {"right": False, "left": False}
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    directions['right'] = True
                elif event.key == pygame.K_a:
                    directions['left'] = True
                if event.key == pygame.K_w:
                    speed += 1
                if event.key == pygame.K_s:
                    if speed != 3:
                        speed -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    directions['right'] = False
                elif event.key == pygame.K_a:
                    directions['left'] = False
        if directions['right']:
            if car.rect.x <= 346:
                car.rect.x += 3
        if directions['left']:
            if car.rect.x >= 10:
                car.rect.x -= 3
        # if pygame.key.get_pressed()[K_w]:
        #     speed += 1
        # if pygame.key.get_pressed()[K_s]:
        #     speed -= 1
        # if pygame.key.get_pressed()[K_a]:
        #     if car.rect.x != 10:
        #         car.rect.x -= 4
        # if pygame.key.get_pressed()[K_d]:
        #     if car.rect.x != 346:
        #         car.rect.x += 4
        if car.rect.x >= 220:
            car.image = load_image("real_car2.png")
        if car.rect.x <= 120:
            car.image = load_image("real_car.png")
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        sprite1.rect.y += speed
        sprite2.rect.y += speed
        if sprite1.rect.y >= 796 - speed - 1:  # если уходит за экран
            sprite1.rect.y = -797
        if sprite2.rect.y >= 796 - speed - 1:
            sprite2.rect.y = -797
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
