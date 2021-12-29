import pygame
import os
import sys
import random
from pygame.locals import *


def load_image(name, colorkey=None):  # открытие картинки
    fullname = os.path.join('picturs', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()  # создаем окно
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
    main_car_group = pygame.sprite.Group()
    car = pygame.sprite.Sprite()
    car.image = load_image("mask.png")
    car.rect = car.image.get_rect()
    car.image = load_image("real_car.png")
    main_car_group.add(car)
    car.rect.x = 160
    car.rect.y = 800  # 800
    # машины по дороге
    car_road = pygame.sprite.Group()
    for i in range(7):
        car_r = pygame.sprite.Sprite()
        car_r.image = load_image(f"roud_car_{random.randint(1, 5)}.png")
        car_r.rect = car.image.get_rect()
        car_road.add(car_r)
        qq = random.randint(1, 3)
        if qq == 1:
            car_r.rect.x = 10 + random.randint(1, 3) * 25
        elif qq == 2:
            car_r.rect.x = 140 + random.randint(1, 3) * 20
        else:
            car_r.rect.x = 290 + random.randint(1, 3) * 10
        car_r.rect.y = -130 * i - 100

    speed = 3  # скорость машинки
    directions = {"right": False, "left": False}  # служит для перемещения машинки
    start = False
    k = 0  # не обращай внимание
    z = 0
    while running:
        if start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:  # управление машинки
                    if event.key == pygame.K_d:
                        directions['right'] = True
                    elif event.key == pygame.K_a:
                        directions['left'] = True
                    if event.key == pygame.K_w:  # управление скорости
                        speed += 1
                    if event.key == pygame.K_s:
                        if speed != 3:
                            speed -= 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        directions['right'] = False
                    elif event.key == pygame.K_a:
                        directions['left'] = False
            if directions['right']:  # направо
                if car.rect.x <= 346:
                    car.rect.x += 5
            if directions['left']:  # налево
                if car.rect.x >= 10:
                    car.rect.x -= 5
            if car.rect.x >= 220:  # изменение изображения
                car.image = load_image("real_car2.png")
            if car.rect.x <= 120:
                car.image = load_image("real_car.png")
        else:
            car.rect.y -= 5
            if car.rect.y <= 500:
                start = True
                k = 60  # для показа START GAME
                z = 100
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        main_car_group.draw(screen)
        sprite1.rect.y += speed
        sprite2.rect.y += speed
        if sprite1.rect.y >= 796 - speed - 1:  # если уходит за экран фон
            sprite1.rect.y = -797
        if sprite2.rect.y >= 796 - speed - 1:
            sprite2.rect.y = -797
        if start:
            if k > 0:
                k -= 1
                # рисуем start
                font = pygame.font.Font(None, 80)
                text = font.render("START GAME", True, (255, 204, 0))
                screen.blit(text, [20, 400])
            for i in car_road:
                i.rect.y += speed
                if i.rect.y >= 796:
                    qq = random.randint(1, 3)
                    if qq == 1:
                        i.rect.x = 10 + random.randint(1, 3) * 25
                    elif qq == 2:
                        i.rect.x = 140 + random.randint(1, 3) * 20
                    else:
                        i.rect.x = 290 + random.randint(1, 3) * 10
                    i.rect.y = -120
                    i.image = load_image(f"roud_car_{random.randint(1, 5)}.png")
            if pygame.sprite.spritecollideany(car, car_road):
                print('ЯРИК пиздец науй')
            car_road.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
