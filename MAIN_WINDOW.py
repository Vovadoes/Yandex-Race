import pygame
import os
import sys
import random
import time
from Car import Car
from Road import Road
from Save import Save
from Starter import Starter
from Map_display import map_display


def load_image(name, colorkey=None):  # открытие картинки
    fullname = os.path.join('picturs', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_image_free(name, colorkey=None):  # открытие картинки
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


indent_x = 571
png_files = {'break_car_taxi_2.png': load_image("break_car_taxi_2.png"),
             'break_car_taxi_1.png': load_image("break_car_taxi_1.png"),
             'real_car.png': load_image("real_car.png"),
             'real_car2.png': load_image("real_car2.png"),
             'break_car_road.png': load_image("break_car_road.png"),
             'legend.png': load_image("legend.png"),
             'roud_car_1.png': load_image(f"roud_car_1.png"),
             'roud_car_2.png': load_image(f"roud_car_2.png"),
             'roud_car_3.png': load_image(f"roud_car_3.png"),
             'roud_car_4.png': load_image(f"roud_car_4.png"),
             'roud_car_5.png': load_image(f"roud_car_5.png"), '0_up.png': load_image(f"0_up.png"),
             '1_up.png': load_image(f"1_up.png"), '2_up.png': load_image(f"2_up.png"),
             '3_up.png': load_image(f"3_up.png"), '4_up.png': load_image(f"4_up.png"),
             '5_up.png': load_image(f"5_up.png"), '6_up.png': load_image(f"6_up.png"),
             'speed_0.png': load_image(f"speed_0.png"), 'speed_1.png': load_image(f"speed_1.png"),
             'speed_2.png': load_image(f"speed_2.png"),
             'speed_3.png': load_image(f"speed_3.png"), 'speed_4.png': load_image(f"speed_4.png"),
             'speed_5.png': load_image(f"speed_5.png"), 'speed_6.png': load_image(f"speed_6.png"),
             'speed_7.png': load_image(f"speed_7.png"), 'speed_8.png': load_image(f"speed_8.png"),
             'speed_9.png': load_image(f"speed_9.png"), 'speed_10.png': load_image(f"speed_10.png"),
             'speed_11.png': load_image(f"speed_11.png"),
             'speed_12.png': load_image(f"speed_12.png"),
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
             'tree_19.png': load_image(f"tree_19.png"), 'hill.png': load_image(f"hill.png"),
             'shild.png': load_image(f"shild.png"), 'money_0.png': load_image(f"money\money_0.png"),
             'money_1.png': load_image(f"money\money_1.png"),
             'money_2.png': load_image(f"money\money_2.png"),
             'money_3.png': load_image(f"money\money_3.png"),
             'money_4.png': load_image(f"money\money_4.png"),
             'money_5.png': load_image(f"money\money_5.png"),
             'money_6.png': load_image(f"money\money_6.png"),
             'money_7.png': load_image(f"money\money_7.png"),
             'nothing.png': load_image(f"nothing.png"),
             'fon.jpg': load_image(f"fon.jpg")}


def show_up_info(up_info, screen, health=0, time_s=0, distance=0):
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
    if time_s <= 0:
        time_s = 0
    if time_s % 60 < 10:
        text = time_sh.render(f"{time_s // 60}:0{time_s % 60}", True, (255, 204, 0))
    else:
        text = time_sh.render(f"{time_s // 60}:{time_s % 60}", True, (255, 204, 0))
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


def pausa(screen, distance, time_road, start_time1, start_time2, koll_money):
    x_pere = 409
    screen.fill((0, 0, 0))
    image = pygame.image.load('picturs\mod_fon.jpg').convert_alpha()
    screen.blit(image, (409, 0))
    pygame.draw.rect(screen, (232, 197, 174),
                     (x_pere + 180, 180, 420, 400))
    # надпись
    font = pygame.font.Font(None, 40)
    text = font.render("TIME LEFT  - ", True, (128, 0, 255))
    screen.blit(text, [x_pere + 210, 240])
    text = font.render("DISTANCE LEFT  - ", True, (128, 0, 255))
    screen.blit(text, [x_pere + 210, 310])
    text = font.render("MONEY EARNED  - ", True, (128, 0, 255))
    screen.blit(text, [x_pere + 210, 380])
    text = font.render("EXIT  -  ESC", True, (255, 79, 0))
    screen.blit(text, [x_pere + 210, 450])
    text = font.render("CONTINUE  -  SPACE", True, (255, 79, 0))
    screen.blit(text, [x_pere + 210, 510])
    font = pygame.font.Font(None, 50)
    if time_road % 60 < 10:
        text = font.render(f"{time_road // 60}:0{time_road % 60}", True, (255, 36, 0))
        screen.blit(text, [x_pere + 400, 240])
    else:
        text = font.render(f"{time_road // 60}:{time_road % 60}", True, (255, 36, 0))
        screen.blit(text, [x_pere + 400, 240])
    text = font.render(f"{round(distance)} m", True, (255, 36, 0))
    screen.blit(text, [x_pere + 460, 305])
    text = font.render(f'{koll_money}', True, (255, 36, 0))  # кол-во денег
    screen.blit(text, [x_pere + 480, 375])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # управление машинки
                if event.key == pygame.K_SPACE:
                    return time.time() - start_time1 - start_time2, False
                elif event.key == pygame.K_ESCAPE:
                    return time.time() - start_time1 - start_time2, True


def whehe_should_put(qq):
    if qq == 1:
        return 5 + 2 * 25
    elif qq == 2:
        return 135 + 2 * 20
    else:
        return 245 + 2 * 25


def end_game(screen, distance, time_rr, money_k, winning_money, save):  # конец игры если прогиграл
    time_rr = round(time_rr)
    picture = pygame.image.load("picturs/you_loss.png")
    screen.blit(picture, (571, 90))
    font = pygame.font.Font(None, 35)
    if time_rr % 60 < 10:
        text = font.render(f"TIME SPENT = {int(time_rr // 60)}:0{time_rr % 60}", True, (255, 204, 0))
        screen.blit(text, [600, 200])
    else:
        text = font.render(f"TIME SPENT = {int(time_rr // 60)}:{time_rr % 60}", True, (255, 204, 0))
        screen.blit(text, [600, 200])
    text = font.render(f"DICTANCE = {int(distance)} m", True, (255, 204, 0))
    screen.blit(text, [600, 240])
    text = font.render(f"MONEY YOU CAUGHT = {money_k}", True, (255, 204, 0))
    screen.blit(text, [600, 280])
    text = font.render(f"MONEY YOU LOSS = {winning_money}", True, (255, 204, 0))
    screen.blit(text, [600, 320])
    text = font.render("НАЖМИТЕ SPACE", True, (255, 0, 51))
    screen.blit(text, [650, 370])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # управление машинки
                if event.key == pygame.K_SPACE:
                    return money_k
                elif event.key == pygame.K_ESCAPE:
                    return money_k


def win_game(screen, distance, time_rr, money_k, winning_money, save):  # конец игры если win
    time_rr = round(time_rr)
    picture = pygame.image.load("picturs/you_won.png")
    screen.blit(picture, (571, 90))
    font = pygame.font.Font(None, 35)
    if time_rr % 60 < 10:
        text = font.render(f"TIME SPENT = {int(time_rr // 60)}:0{time_rr % 60}", True, (255, 204, 0))
        screen.blit(text, [600, 200])
    else:
        text = font.render(f"TIME SPENT = {int(time_rr // 60)}:{time_rr % 60}", True, (255, 204, 0))
        screen.blit(text, [600, 200])
    text = font.render(f"DICTANCE = {distance}", True, (255, 204, 0))
    screen.blit(text, [600, 240])
    text = font.render(f"MONEY YOU CAUGHT = {money_k}", True, (255, 204, 0))
    screen.blit(text, [600, 280])
    text = font.render(f"ALL MONEY = {money_k + winning_money}", True, (255, 204, 0))
    screen.blit(text, [600, 320])
    text = font.render("НАЖМИТЕ SPACE", True, (255, 0, 51))
    screen.blit(text, [650, 370])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # управление машинки
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    return money_k + winning_money


def main_game(screen, size: tuple[int, int], save: Save, road: Road, car_obj: Car):
    left_pictur = car_obj.images[0].last_image.path
    right_pictur = car_obj.images[-1].last_image.path
    rect_pictur = car_obj.mask.last_image.path
    max_speed = car_obj.specifications["max_speed"]
    time_run = car_obj.specifications["boost"]  # разгон
    limited_time = road.set_time(road.distance / road.specifications.PX_KM)
    distance = (road.distance * 1000) // road.specifications.PX_KM
    winning_money = round(road.money * car_obj.class_car.k_money)
    # screen, size: tuple[int, int], save: Save, road: Road, car: Car
    # winning_money = 100  # деньги которые он выйграет
    indent_x = 571
    animation_set = [pygame.image.load(f"picturs\money\money_{i}.png") for i in range(0, 8)]
    # pygame.init()  # создаем окно
    # pygame.display.set_caption('Yandex_Race')
    # size = width, height = 400 + 571 * 2, 799
    # screen = pygame.display.set_mode(size)

    running = True
    fps = 60  # пикселей в секунду
    clock = pygame.time.Clock()
    # фон левый и правый
    fon = pygame.sprite.Group()
    fon_left = pygame.sprite.Sprite()
    fon_left.image = png_files["fon.jpg"]
    fon_left.rect = fon_left.image.get_rect()
    fon.add(fon_left)
    fon_left.rect.x = 0
    fon_left.rect.y = 0
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
    sprite_side_road1.rect.x = 571 - 160
    sprite_side_road1.rect.y = 0
    # левый второй край
    sprite_side_road3 = pygame.sprite.Sprite()
    sprite_side_road3.image = load_image("trava_3.png")
    sprite_side_road3.rect = sprite_side_road3.image.get_rect()
    side_road_left.add(sprite_side_road3)
    sprite_side_road3.rect.x = 571 - 160
    sprite_side_road3.rect.y = -798
    # правый первый край
    side_road_right = pygame.sprite.Group()
    sprite_side_road2 = pygame.sprite.Sprite()
    sprite_side_road2.image = load_image("trava_4.png")
    sprite_side_road2.rect = sprite_side_road2.image.get_rect()
    side_road_right.add(sprite_side_road2)
    sprite_side_road2.rect.x = 400 + 571
    sprite_side_road2.rect.y = 0
    # правый второй край
    sprite_side_road4 = pygame.sprite.Sprite()
    sprite_side_road4.image = load_image("trava_4.png")
    sprite_side_road4.rect = sprite_side_road4.image.get_rect()
    side_road_right.add(sprite_side_road4)
    sprite_side_road4.rect.x = 400 + 571
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
    car.image = load_image_free(rect_pictur)
    car.rect = car.image.get_rect()
    car.image = load_image_free(left_pictur)
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
        tree.rect.x = 10 + indent_x - 162
        tree.rect.y = -160 * i - 100
    tree_group_2 = pygame.sprite.Group()
    for i in range(5):
        tree = pygame.sprite.Sprite()
        tree.image = png_files[f"tree_{random.randint(1, 19)}.png"]
        tree.rect = car.image.get_rect()
        tree_group_2.add(tree)
        tree.rect.x = 580 + indent_x - 162
        tree.rect.y = -200 * i
    # бонусы
    hill_group = pygame.sprite.Group()
    hill = pygame.sprite.Sprite()
    hill.image = png_files['hill.png']
    hill.rect = car.image.get_rect()
    hill_group.add(hill)
    hill.rect.x = 0
    hill.rect.y = - 64

    shild_group = pygame.sprite.Group()
    shild = pygame.sprite.Sprite()
    shild.image = png_files['shild.png']
    shild.rect = car.image.get_rect()
    shild_group.add(shild)
    shild.rect.x = 0
    shild.rect.y = - 64

    money_group = pygame.sprite.Group()
    money = pygame.sprite.Sprite()
    money.image = png_files['money_0.png']
    money.rect = money.image.get_rect()
    money_group.add(money)
    money.rect.x = 0
    money.rect.y = - 64

    speed = 3  # скорость машинки
    directions = {"right": False, "left": False}  # служит для перемещения машинки
    start = False
    k = 0  # не обращай внимание
    z = 0
    kol_stol = 0
    health = 6
    sec_neuas = 0
    what_was = left_pictur
    # limited_time = 60  # время на поездку
    start_time = time.time()
    end_time = 0
    # distance = 2000  # дистанцию которую надо пройти
    distance_save = distance  # копия пути
    # музыка
    pygame.mixer.music.load(f'music\music_{random.randint(1, 10)}.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    start_music = pygame.mixer.Sound('music\start_music.mp3')
    end_music = pygame.mixer.Sound('music\music_end.mp3')
    music_boom = pygame.mixer.Sound('music\music_boom.mp3')
    motor_music = pygame.mixer.Sound('music\motor.mp3')
    music_boom.set_volume(0.4)
    motor_music.set_volume(0.3)
    speed_time_limit = 0
    musiс_bonus_1, musiс_bonus_2, musiс_bonus_3 = motor_music, motor_music, motor_music
    # другое
    paus_time = 0
    is_stop = False
    is_end = False
    is_hill_in = False
    is_shild_in = False
    is_money_in = False
    koll_money = 0
    vois_down = 0  # int(1.5 * fps)
    bonus_music = True
    money_k = 0
    is_win = False
    peremen = 90  # для сбавления скорости
    peremen_2 = 6 * fps  # для конечного экрана
    while running:
        if health == 0:
            speed = 0
            if what_was == left_pictur:
                for i in main_car_group:
                    i.image = png_files['break_car_taxi_2.png']
            elif what_was == right_pictur:
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
                if not is_win:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN:  # управление машинки
                            if event.key == pygame.K_d:
                                directions['right'] = True
                            elif event.key == pygame.K_a:
                                directions['left'] = True
                            if event.key == pygame.K_w and speed_time_limit == 0 and speed != max_speed:  # управление скорости
                                speed += 1
                                pygame.mixer.Sound.play(motor_music)
                                speed_time_limit = int(time_run * fps)
                            if event.key == pygame.K_s:
                                if speed != 3:
                                    speed -= 1
                            if event.key == pygame.K_x:
                                if bonus_music:
                                    bonus_music = False
                                else:
                                    bonus_music = True
                            if event.key == pygame.K_z:
                                pygame.mixer.music.load(f'music\music_{random.randint(1, 10)}.mp3')
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play()
                            if event.key == pygame.K_SPACE:
                                pygame.mixer.music.pause()
                                rrr, is_end = pausa(screen, distance,
                                                    round(limited_time - (
                                                            time.time() - start_time - paus_time)),
                                                    start_time, time.time() - start_time, koll_money)
                                pygame.mixer.music.unpause()
                                paus_time += rrr
                            if event.key == pygame.K_ESCAPE:
                                is_end = True
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
                        car.image = load_image_free(right_pictur)
                        what_was = right_pictur
                    if car.rect.x <= 120 + indent_x and sec_neuas == 0:
                        car.image = load_image_free(left_pictur)
                        what_was = left_pictur
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        # if event.type == pygame.KEYDOWN:
                        #     if event.key == pygame.K_d:
                        #         directions['right'] = True
                    if car.rect.x <= 346 + indent_x:
                        car.rect.x += 1
                    if peremen_2 != 0:
                        peremen_2 -= 1
                    else:
                        return win_game(screen, distance_save,
                                        time.time() - start_time - paus_time - 6, koll_money,
                                        winning_money, save), True
            else:
                pygame.mixer.Sound.play(start_music)
                car.rect.y -= 5
                if car.rect.y <= 500:
                    start = True
                    k = 60  # для показа START GAME
                    z = 100
            screen.fill((0, 0, 0))
            # показ почти всего
            fon.draw(screen)  # left right fon
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
                        # is_hill_in = False
                        # is_shild_in = False
                        # is_money_in = False
                        qq = random.randint(1, 3)
                        bonus = random.randint(1, 100)  # работа с бонусами
                        if bonus in list(range(6, 7)) and not is_hill_in:  # 2%
                            is_hill_in = True
                            for j in hill_group:
                                if qq == 1:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([2, 3]))
                                elif qq == 2:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 3]))
                                else:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 2]))
                        elif bonus in list(range(87, 90)) and not is_shild_in:  # 3%
                            is_shild_in = True
                            for j in shild_group:
                                if qq == 1:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([2, 3]))
                                elif qq == 2:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 3]))
                                else:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 2]))
                        elif bonus in list(range(55, 85)) and not is_money_in:
                            is_money_in = True
                            for j in money_group:
                                if qq == 1:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([2, 3]))
                                elif qq == 2:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 3]))
                                else:
                                    j.rect.x = indent_x + whehe_should_put(random.choice([1, 2]))
                        # бонусы завершены
                        if qq == 1:
                            i.rect.x = 10 + random.randint(1, 3) * 25 + indent_x
                        elif qq == 2:
                            i.rect.x = 140 + random.randint(1, 3) * 20 + indent_x
                        else:
                            i.rect.x = 250 + random.randint(1, 3) * 25 + indent_x
                        i.rect.y = -120
                        if not is_win:
                            i.image = png_files[f"roud_car_{random.randint(1, 5)}.png"]
                        else:
                            i.image = png_files[f"nothing.png"]
                            shild.image = png_files[f"nothing.png"]
                            hill.image = png_files[f"nothing.png"]
                # визуализация бонусов
                if is_hill_in:
                    hill_group.draw(screen)
                    for i in hill_group:
                        i.rect.y += speed
                        if i.rect.y >= 796:
                            is_hill_in = False
                            i.rect.y = -120
                if is_shild_in:
                    shild_group.draw(screen)
                    for i in shild_group:
                        i.rect.y += speed
                        if i.rect.y >= 796:
                            is_shild_in = False
                            i.rect.y = -120
                if is_money_in:
                    money_group.draw(screen)
                    for i in money_group:
                        i.rect.y += speed
                        if i.rect.y >= 796:
                            is_money_in = False
                            i.rect.y = -120

                # маневр века
                for i in main_car_group:
                    car.rect.x += 20
                    car.rect.y += 20
                if pygame.sprite.spritecollideany(car,
                                                  car_road) and sec_neuas == 0:  # сталкивание с машиной
                    blocks_hit_list = pygame.sprite.spritecollide(car, car_road, False)
                    blocks_hit_list[0].image = png_files["break_car_road.png"]
                    kol_stol += 1
                    health -= 1
                    if health == 0:
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(end_music)
                        is_end = True
                    else:
                        pygame.mixer.Sound.play(music_boom)
                    sec_neuas = 2 * fps  # бесмертие
                    print(kol_stol)
                    print(blocks_hit_list)
                    end_time = round(
                        limited_time - (time.time() - start_time - paus_time))  # запечатлить время
                for i in main_car_group:
                    car.rect.x -= 20
                    car.rect.y -= 20

                if sec_neuas != 0:  # управление бесмертием
                    sec_neuas -= 1
                    car.image = png_files["legend.png"]
                else:
                    car.image = load_image_free(what_was)
                # взаимодействие с бонусами
                if not is_win:
                    if pygame.sprite.spritecollideany(car, hill_group):
                        for i in hill_group:
                            i.rect.y = -120
                            is_hill_in = False
                            if health != 6:
                                health += 1
                        if bonus_music:
                            musiс_bonus_2.stop()
                            musiс_bonus_3.stop()
                            musiс_bonus_1 = pygame.mixer.Sound(
                                f'music\аптечка_{random.randint(1, 4)}.mp3')
                            musiс_bonus_1.set_volume(3)
                            vois_down = int(2 * fps)
                            pygame.mixer.Sound.play(musiс_bonus_1)
                    if pygame.sprite.spritecollideany(car, money_group):
                        for i in money_group:
                            i.rect.y = -120
                            is_money_in = False
                            koll_money += 1
                        if bonus_music:
                            musiс_bonus_1.stop()
                            musiс_bonus_3.stop()
                            musiс_bonus_2 = pygame.mixer.Sound(
                                f'music\деньги_{random.randint(1, 5)}.mp3')
                            musiс_bonus_2.set_volume(3)
                            vois_down = int(2 * fps)
                            pygame.mixer.Sound.play(musiс_bonus_2)
                    if pygame.sprite.spritecollideany(car, shild_group):
                        for i in shild_group:
                            i.rect.y = -120
                            is_shild_in = False
                            sec_neuas = 3 * fps
                        if bonus_music:
                            musiс_bonus_1.stop()
                            musiс_bonus_2.stop()
                            musiс_bonus_3 = pygame.mixer.Sound(
                                f'music\щит_{random.randint(1, 3)}.mp3')
                            musiс_bonus_3.set_volume(3)
                            vois_down = int(2 * fps)
                            pygame.mixer.Sound.play(musiс_bonus_3)
                if is_money_in:  # летающая денежка
                    money_k += 1
                    if money_k == 60:
                        money_k = 0
                    if not is_win:
                        money.image = animation_set[int(money_k // 7.5)]
                    else:
                        money.image = png_files[f"nothing.png"]
            if vois_down != 0:
                vois_down -= 1
                pygame.mixer.music.set_volume(0.1)
                music_boom.set_volume(0.1)
            else:
                pygame.mixer.music.set_volume(0.5)
                music_boom.set_volume(0.4)
            car_road.draw(screen)
        distance -= speed * 0.1
        if health != 0:
            show_up_info(up_info, screen, 6 - health,
                         round(limited_time - (time.time() - start_time - paus_time)),
                         distance)
            show_speed(speed_info, screen, speed)
        else:
            show_up_info(up_info, screen, 6 - health, end_time, distance)
            show_speed(speed_info, screen, 3)
        if speed_time_limit != 0:
            speed_time_limit -= 1
        if distance <= 0 and not is_end:
            pygame.mixer.music.pause()
            distance = 0
            is_win = True
            sec_neuas = 6 * fps
            peremen -= 1
            if peremen == 0:
                if speed == 1 and peremen_2 >= 300:
                    speed += 1
                if speed != 0:
                    speed -= 1
                peremen = 90
        if limited_time - (time.time() - start_time - paus_time) <= 0 and not is_win:
            is_end = True
        if is_end:
            main_car_group.draw(screen)
            pygame.mixer.music.pause()
            pygame.display.flip()
            print(1234)
            return end_game(screen, distance_save - distance, time.time() - start_time - paus_time,
                            koll_money,
                            winning_money, save), False

        # проверяем чтобы не было отступов
        # if sprite1.rect.y < sprite2.rect.y:  # sprite1 наверху
        #     ras = abs(sprite2.rect.y) + abs(sprite1.rect.y)
        #     print(ras)
        #     if ras != 798:
        #         sprite2.rect.y -= 1
        # else:  # sprite2 наверху
        #     ras = abs(sprite2.rect.y) + abs(sprite1.rect.y)
        #     print(ras)
        #     if ras != 798:
        #         sprite1.rect.y -= 1
        # print(sprite1.rect.y, sprite2.rect.y)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


# left_pictur, right_pictur, rect_pictur, max_speed, time_run, limited_time, distance, winning_money
# print(main_game("real_car.png", 'real_car2.png', 'mask.png', 7, 1, 60, 2000, 50))

def start_game(screen, size: tuple[int, int], save: Save, road: Road, car_obj: Car):
    screen_new = pygame.display.set_mode((1542, 799))
    # money, finished = main_game(screen_new, (1542, 799), save, road, car_obj)
    money, finished = 10, False
    if finished:
        save.specifications.money += money
    road.complete_trip = True
    car_obj.images = []
    car_obj.mask = None
    car_obj.basic_image = None
    save.road_and_car[road] = car_obj
    print(save.road_and_car)
    save.save()
    starter = Starter(map_display, screen, size, save)
    return starter
