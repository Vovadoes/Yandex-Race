import pygame
import os
import sys
import random
import time
from pygame.locals import *


def load_image(name, colorkey=None):  # открытие картинки
    fullname = os.path.join('picturs', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def show_up_info(up_info, screen, health=0, time=0, distance=0):
    if health != 0:
        for i in up_info:
            if health == 1:
                i.image = png_files["1_up.png"]
            elif health == 2:
                i.image = png_files["2_up.png"]
            elif health == 3:
                i.image = png_files["3_up.png"]
            elif health == 4:
                i.image = png_files["4_up.png"]
            elif health == 5:
                i.image = png_files["5_up.png"]
            elif health == 6:
                i.image = png_files["6_up.png"]
    up_info.draw(screen)
    time_sh = pygame.font.Font(None, 40)
    text = time_sh.render(f"{time // 60}:{time % 60}", True, (255, 204, 0))
    screen.blit(text, [170, 5])

    distance_sh = pygame.font.Font(None, 30)
    text = distance_sh.render(f"{round(distance)} m", True, (255, 204, 0))
    screen.blit(text, [293, 2])


def show_speed(up_info, screen, speed=0):
    for i in up_info:
        i.image = png_files[f"speed_{speed}.png"]
    up_info.draw(screen)


if __name__ == '__main__':
    png_files = {'break_car_taxi_2.png': load_image("break_car_taxi_2.png"),
                 'break_car_taxi_1.png': load_image("break_car_taxi_1.png"),
                 'real_car.png': load_image("real_car.png"), 'real_car2.png': load_image("real_car2.png"),
                 'break_car_road.png': load_image("break_car_road.png"), 'legend.png': load_image("legend.png"),
                 'roud_car_1.png': load_image(f"roud_car_1.png"), 'roud_car_2.png': load_image(f"roud_car_2.png"),
                 'roud_car_3.png': load_image(f"roud_car_3.png"), 'roud_car_4.png': load_image(f"roud_car_4.png"),
                 'roud_car_5.png': load_image(f"roud_car_5.png"), '0_up.png': load_image(f"0_up.png"),
                 '1_up.png': load_image(f"1_up.png"), '2_up.png': load_image(f"2_up.png"),
                 '3_up.png': load_image(f"3_up.png"), '4_up.png': load_image(f"4_up.png"),
                 '5_up.png': load_image(f"5_up.png"), '6_up.png': load_image(f"6_up.png"),
                 'speed_3.png': load_image(f"speed_3.png"), 'speed_4.png': load_image(f"speed_4.png"),
                 'speed_5.png': load_image(f"speed_5.png"), 'speed_6.png': load_image(f"speed_6.png"),
                 'speed_7.png': load_image(f"speed_7.png"), 'speed_8.png': load_image(f"speed_8.png"),
                 'speed_9.png': load_image(f"speed_9.png"), 'speed_10.png': load_image(f"speed_10.png"),
                 'speed_11.png': load_image(f"speed_11.png"), 'speed_12.png': load_image(f"speed_12.png")}
    pygame.init()  # создаем окно
    pygame.display.set_caption('Yandex_Race')
    size = width, height = 400, 799
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60  # пикселей в секунду
    clock = pygame.time.Clock()

    # главная информация
    up_info = pygame.sprite.Group()
    sprite_up = pygame.sprite.Sprite()
    sprite_up.image = png_files["0_up.png"]
    sprite_up.rect = sprite_up.image.get_rect()
    up_info.add(sprite_up)
    sprite_up.rect.x = 0
    sprite_up.rect.y = 0
    # скорость игрока
    speed_info = pygame.sprite.Group()
    sprite_speed = pygame.sprite.Sprite()
    sprite_speed.image = png_files["speed_3.png"]
    sprite_speed.rect = sprite_speed.image.get_rect()
    speed_info.add(sprite_speed)
    sprite_speed.rect.x = 280
    sprite_speed.rect.y = 30
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
    car.image = png_files["real_car.png"]
    main_car_group.add(car)
    car.rect.x = 160  # 160
    car.rect.y = 800  # 800
    # машины по дороге
    car_road = pygame.sprite.Group()
    for i in range(7):
        car_r = pygame.sprite.Sprite()
        car_r.image = png_files[f"roud_car_{random.randint(1, 5)}.png"]
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
    kol_stol = 0
    health = 6
    sec_neuas = 0
    what_was = 'real_car.png'
    limited_time = 340  # время на поездку
    start_time = time.time()
    end_time = 0
    distance = 2000  # дистанцию которую надо пройти
    while running:
        if health == 0:
            speed = 0
            if what_was == 'real_car.png':
                for i in main_car_group:
                    i.image = png_files['break_car_taxi_2.png']
            elif what_was == 'real_car2.png':
                for i in main_car_group:
                    i.image = png_files["break_car_taxi_1.png"]
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            main_car_group.draw(screen)
            car_road.draw(screen)

            font = pygame.font.Font(None, 80)
            text = font.render("GAME OVER", True, (255, 204, 0))
            screen.blit(text, [30, 400])

            clock.tick(fps)
            pygame.display.flip()
        else:
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
                if car.rect.x >= 220 and sec_neuas == 0:  # изменение изображения
                    car.image = png_files["real_car2.png"]
                    what_was = 'real_car2.png'
                if car.rect.x <= 120 and sec_neuas == 0:
                    car.image = png_files["real_car.png"]
                    what_was = 'real_car.png'
            else:
                car.rect.y -= 5
                if car.rect.y <= 500:
                    start = True
                    k = 60  # для показа START GAME
                    z = 100
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            main_car_group.draw(screen)
            # управление фоном
            sprite1.rect.y += speed
            sprite2.rect.y += speed
            if sprite1.rect.y >= 796 - speed - 1:  # если уходит за экран фон
                sprite1.rect.y = -797
            if sprite2.rect.y >= 796 - speed - 1:
                sprite2.rect.y = -797
            if start:  # main
                if k > 0:  # рисуем start
                    k -= 1
                    font = pygame.font.Font(None, 80)
                    text = font.render("START GAME", True, (255, 204, 0))
                    screen.blit(text, [20, 400])
                for i in car_road:  # если машина ушла с трассы
                    i.rect.y += speed
                    if i.rect.y >= 796:
                        qq = random.randint(1, 3)
                        if qq == 1:
                            i.rect.x = 10 + random.randint(1, 3) * 25
                        elif qq == 2:
                            i.rect.x = 140 + random.randint(1, 3) * 20
                        else:
                            i.rect.x = 250 + random.randint(1, 3) * 25
                        i.rect.y = -120
                        i.image = png_files[f"roud_car_{random.randint(1, 5)}.png"]
                # маневр века
                for i in main_car_group:
                    car.rect.x += 20
                    car.rect.y += 20
                if pygame.sprite.spritecollideany(car, car_road) and sec_neuas == 0:  # сталкивание с машиной
                    blocks_hit_list = pygame.sprite.spritecollide(car, car_road, False)
                    blocks_hit_list[0].image = png_files["break_car_road.png"]
                    kol_stol += 1
                    health -= 1
                    sec_neuas = 2 * fps  # бесмертие
                    print(kol_stol)
                    print(blocks_hit_list)
                    end_time = round(limited_time - (time.time() - start_time))  # запечатлить время
                for i in main_car_group:
                    car.rect.x -= 20
                    car.rect.y -= 20

                if sec_neuas != 0:  # управление бесмертием
                    sec_neuas -= 1
                    car.image = png_files["legend.png"]
                else:
                    car.image = png_files[what_was]
            car_road.draw(screen)
        distance -= speed * 0.1
        if health != 0:
            show_up_info(up_info, screen, 6 - health, round(limited_time - (time.time() - start_time)), distance)
            show_speed(speed_info, screen, speed)
        else:
            show_up_info(up_info, screen, 6 - health, end_time, distance)
            show_speed(speed_info, screen, speed)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
