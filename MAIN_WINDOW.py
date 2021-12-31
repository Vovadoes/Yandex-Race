import pygame
import os
import sys
import random
import time
from threading import *
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
    if time % 60 < 10:
        text = time_sh.render(f"{time // 60}:0{time % 60}", True, (255, 204, 0))
    else:
        text = time_sh.render(f"{time // 60}:{time % 60}", True, (255, 204, 0))
    screen.blit(text, [170 + indent_x, 5])

    distance_sh = pygame.font.Font(None, 30)
    text = distance_sh.render(f"{round(distance)} m", True, (255, 204, 0))
    screen.blit(text, [293 + indent_x, 2])


def show_speed(up_info, screen, speed=0):
    for i in up_info:
        if speed <= 12:
            i.image = png_files[f"speed_{speed}.png"]
    up_info.draw(screen)


def show_fon_trees(group, screen, speed):
    for i in group:
        i.rect.y += speed
        if i.rect.y >= 796 - speed - 1:  # если уходит за экран фон
            i.rect.y = -797


def show_fon_trees_real(group, screen, speed):
    for i in group:
        i.rect.y += speed
        if i.rect.y >= 796:
            i.rect.y = -170
            i.image = png_files[f"tree_{random.randint(1, 19)}.png"]


if __name__ == '__main__':
    indent_x = 162
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
                 'speed_11.png': load_image(f"speed_11.png"), 'speed_12.png': load_image(f"speed_12.png"),
                 'trava_3.png': load_image(f"trava_3.png"), 'trava_4.png': load_image(f"trava_4.png"),
                 'tree_1.png': load_image(f"tree_1.png"), 'tree_2.png': load_image(f"tree_2.png"),
                 'tree_3.png': load_image(f"tree_3.png"), 'tree_4.png': load_image(f"tree_4.png"),
                 'tree_5.png': load_image(f"tree_5.png"), 'tree_6.png': load_image(f"tree_6.png"),
                 'tree_7.png': load_image(f"tree_7.png"), 'tree_8.png': load_image(f"tree_8.png"),
                 'tree_9.png': load_image(f"tree_9.png"), 'tree_10.png': load_image(f"tree_10.png"),
                 'tree_11.png': load_image(f"tree_11.png"), 'tree_12.png': load_image(f"tree_12.png"),
                 'tree_13.png': load_image(f"tree_13.png"), 'tree_14.png': load_image(f"tree_14.png"),
                 'tree_15.png': load_image(f"tree_15.png"), 'tree_16.png': load_image(f"tree_16.png"),
                 'tree_17.png': load_image(f"tree_17.png"), 'tree_18.png': load_image(f"tree_18.png"),
                 'tree_19.png': load_image(f"tree_19.png")}
    pygame.init()  # создаем окно
    pygame.display.set_caption('Yandex_Race')
    size = width, height = 400 + 162 * 2, 799
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
    sprite_up.rect.x = 0 + indent_x
    sprite_up.rect.y = 0
    # скорость игрока
    speed_info = pygame.sprite.Group()
    sprite_speed = pygame.sprite.Sprite()
    sprite_speed.image = png_files["speed_3.png"]
    sprite_speed.rect = sprite_speed.image.get_rect()
    speed_info.add(sprite_speed)
    sprite_speed.rect.x = 280 + indent_x
    sprite_speed.rect.y = 30
    # левый первый край
    side_road_left = pygame.sprite.Group()
    sprite_side_road1 = pygame.sprite.Sprite()
    sprite_side_road1.image = load_image("trava_3.png")
    sprite_side_road1.rect = sprite_side_road1.image.get_rect()
    side_road_left.add(sprite_side_road1)
    sprite_side_road1.rect.x = 0
    sprite_side_road1.rect.y = 0
    # левый второй край
    sprite_side_road3 = pygame.sprite.Sprite()
    sprite_side_road3.image = load_image("trava_3.png")
    sprite_side_road3.rect = sprite_side_road3.image.get_rect()
    side_road_left.add(sprite_side_road3)
    sprite_side_road3.rect.x = 0
    sprite_side_road3.rect.y = -798
    # правый первый край
    side_road_right = pygame.sprite.Group()
    sprite_side_road2 = pygame.sprite.Sprite()
    sprite_side_road2.image = load_image("trava_4.png")
    sprite_side_road2.rect = sprite_side_road2.image.get_rect()
    side_road_right.add(sprite_side_road2)
    sprite_side_road2.rect.x = 400 + indent_x
    sprite_side_road2.rect.y = 0
    # правый второй край
    sprite_side_road4 = pygame.sprite.Sprite()
    sprite_side_road4.image = load_image("trava_4.png")
    sprite_side_road4.rect = sprite_side_road4.image.get_rect()
    side_road_right.add(sprite_side_road4)
    sprite_side_road4.rect.x = 400 + indent_x
    sprite_side_road4.rect.y = -798
    # первая дорога
    all_sprites = pygame.sprite.Group()
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = load_image("3_polos.png")
    sprite1.rect = sprite1.image.get_rect()
    all_sprites.add(sprite1)
    sprite1.rect.x = 0 + indent_x
    sprite1.rect.y = 0
    # вторая дорога
    sprite2 = pygame.sprite.Sprite()
    sprite2.image = load_image("3_polos.png")
    sprite2.rect = sprite2.image.get_rect()
    all_sprites.add(sprite2)
    sprite2.rect.x = 0 + indent_x
    sprite2.rect.y = -798
    # машинка
    main_car_group = pygame.sprite.Group()
    car = pygame.sprite.Sprite()
    car.image = load_image("mask.png")
    car.rect = car.image.get_rect()
    car.image = png_files["real_car.png"]
    main_car_group.add(car)
    car.rect.x = 160 + indent_x  # 160
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
            car_r.rect.x = 10 + random.randint(1, 3) * 25 + indent_x
        elif qq == 2:
            car_r.rect.x = 140 + random.randint(1, 3) * 20 + indent_x
        else:
            car_r.rect.x = 290 + random.randint(1, 3) * 10 + indent_x
        car_r.rect.y = -130 * i - 100
    # растения по дороге
    tree_group_1 = pygame.sprite.Group()
    for i in range(5):
        tree = pygame.sprite.Sprite()
        tree.image = png_files[f"tree_{random.randint(1, 19)}.png"]
        tree.rect = car.image.get_rect()
        tree_group_1.add(tree)
        tree.rect.x = 10
        tree.rect.y = -160 * i - 100
    tree_group_2 = pygame.sprite.Group()
    for i in range(5):
        tree = pygame.sprite.Sprite()
        tree.image = png_files[f"tree_{random.randint(1, 19)}.png"]
        tree.rect = car.image.get_rect()
        tree_group_2.add(tree)
        tree.rect.x = 580
        tree.rect.y = -200 * i

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
    # музыка
    start_music = pygame.mixer.Sound('music\start_music.mp3')
    main_music = pygame.mixer.Sound(f'music\music_{random.randint(1, 10)}.mp3')
    main_music.set_volume(0.5)
    end_music = pygame.mixer.Sound('music\music_end.mp3')
    music_boom = pygame.mixer.Sound('music\music_boom.mp3')
    motor_music = pygame.mixer.Sound('music\motor.mp3')
    pygame.mixer.Sound.play(main_music)
    speed_time_limit = 0
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
            side_road_left.draw(screen)
            side_road_right.draw(screen)
            main_car_group.draw(screen)
            car_road.draw(screen)
            tree_group_1.draw(screen)
            tree_group_2.draw(screen)

            font = pygame.font.Font(None, 80)
            text = font.render("GAME OVER", True, (255, 204, 0))
            screen.blit(text, [30 + indent_x, 400])
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
                        if event.key == pygame.K_w and speed_time_limit == 0:  # управление скорости
                            speed += 1
                            pygame.mixer.Sound.play(motor_music)
                            speed_time_limit = 180
                        if event.key == pygame.K_s:
                            if speed != 3:
                                speed -= 1
                        if event.key == pygame.K_z:
                            pygame.mixer.Sound.stop(main_music)
                            main_music = pygame.mixer.Sound(f'music\music_{random.randint(1, 10)}.mp3')
                            main_music.set_volume(0.5)
                            pygame.mixer.Sound.play(main_music)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            directions['right'] = False
                        elif event.key == pygame.K_a:
                            directions['left'] = False
                if directions['right']:  # направо
                    if car.rect.x <= 346 + indent_x:
                        car.rect.x += 5
                if directions['left']:  # налево
                    if car.rect.x >= 10 + indent_x:
                        car.rect.x -= 5
                if car.rect.x >= 220 + indent_x and sec_neuas == 0:  # изменение изображения
                    car.image = png_files["real_car2.png"]
                    what_was = 'real_car2.png'
                if car.rect.x <= 120 + indent_x and sec_neuas == 0:
                    car.image = png_files["real_car.png"]
                    what_was = 'real_car.png'
            else:
                pygame.mixer.Sound.play(start_music)
                car.rect.y -= 5
                if car.rect.y <= 500:
                    start = True
                    k = 60  # для показа START GAME
                    z = 100
            screen.fill((0, 0, 0))
            # показ почти всего
            all_sprites.draw(screen)
            side_road_left.draw(screen)
            side_road_right.draw(screen)
            main_car_group.draw(screen)
            # изменения левого и правго края
            show_fon_trees(side_road_left, screen, speed)
            show_fon_trees(side_road_right, screen, speed)
            # изменения растений
            tree_group_1.draw(screen)
            tree_group_2.draw(screen)
            show_fon_trees_real(tree_group_1, screen, speed)
            show_fon_trees_real(tree_group_2, screen, speed)
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
                    screen.blit(text, [20 + indent_x, 400])
                for i in car_road:  # если машина ушла с трассы
                    i.rect.y += speed
                    if i.rect.y >= 796:
                        qq = random.randint(1, 3)
                        if qq == 1:
                            i.rect.x = 10 + random.randint(1, 3) * 25 + indent_x
                        elif qq == 2:
                            i.rect.x = 140 + random.randint(1, 3) * 20 + indent_x
                        else:
                            i.rect.x = 250 + random.randint(1, 3) * 25 + indent_x
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
                    if health == 0:
                        pygame.mixer.Sound.stop(main_music)
                        pygame.mixer.Sound.play(end_music)
                    else:
                        pygame.mixer.Sound.play(music_boom)
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
            # Thread(target=car_road.draw, args=(screen,)).start()
            car_road.draw(screen)
        distance -= speed * 0.1
        if health != 0:
            show_up_info(up_info, screen, 6 - health, round(limited_time - (time.time() - start_time)), distance)
            show_speed(speed_info, screen, speed)
        else:
            show_up_info(up_info, screen, 6 - health, end_time, distance)
            show_speed(speed_info, screen, 3)
        if speed_time_limit != 0:
            speed_time_limit -= 1
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
