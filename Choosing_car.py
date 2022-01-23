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
    TEXT_Height = int(4 * k_image_standart)
    X_TEXT_BEGIN = int(0.02 * size[0])
    X_TEXT_END = int(0.4 * size[0])
    Y_BLOCK_BEGIN_TEXT = int(0.64 * size[1])
    Y_BLOCK_END_TEXT = int(0.97 * size[1])
    X_BUTTON = int(0.65 * size[0])
    Y_BUTTON = int(0.9 * size[1])
    X_LOCK_BUTTON = int(0.4 * size[0])
    Y_LOCK_BUTTON = int(0.3 * size[1])

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(background_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background.image, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    cars = []
    for i in os.listdir(os.path.join(Car.path_save)):
        car = Car().load(path=i)
        k = min(size[1] * 0.8 / car.basic_image.rect.height,
                size[0] * 0.8 / car.basic_image.rect.width)
        car.basic_image = Button(car.basic_image.deafult_image, k, k)
        car.basic_image.rect.x = (size[0] - car.basic_image.rect.width) // 2
        car.basic_image.rect.y = (size[1] - car.basic_image.rect.height) // 2
        cars.append(car)

    cars.reverse()

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

    dct_text = {'max_speed': 'Максимальная скорость', 'boost': 'Ускорение'}

    for i in Car.specifications:
        if i in dct_text:
            texts[i] = Text(f"{dct_text[i]}: ", height=TEXT_Height, x=X_TEXT_BEGIN)
            texts[i].value = [Car.specifications[i]]

    texts['you_counts'] = Text(f"Количество монет: ", height=TEXT_Height, x=X_TEXT_BEGIN)
    texts['you_counts'].value = [save.specifications.money]

    dct_message = {'ok': "OK", 'no_money': 'У вас мало денег'}

    texts['message'] = Text(f"Сообщение: ", height=TEXT_Height, x=X_TEXT_BEGIN)
    texts['message'].value = [dct_message['ok']]

    print(texts)

    d_y_text = (Y_BLOCK_END_TEXT - Y_BLOCK_BEGIN_TEXT - (len(texts) * TEXT_Height)) / (
            len(texts) + 1)
    y_text = Y_BLOCK_BEGIN_TEXT + d_y_text
    for i in texts:
        texts[i].y = y_text
        y_text += TEXT_Height + d_y_text

    del d_y_text
    del y_text

    lock_button = Button(Image("data/lock.png"), 1, 1)
    k = min(size[1] * 0.5 / lock_button.rect.height,
            size[0] * 0.5 / lock_button.rect.width)
    lock_button = Button(Image("data/lock.png"), k, k, clok_sprites)
    lock_button.rect.x = X_LOCK_BUTTON
    lock_button.rect.y = Y_LOCK_BUTTON
    lock_button.set_text("Поехали)")

    buy_car = cars[index_car].info["name"] in save.specifications.name_cars

    button_GO_dct = {True: "Поехали)", False: "Купить за {} монет."}
    button_GO = Button(Image("data/Кнопка.png"), 1, 1)
    k = size[1] * 0.08 / button_GO.rect.height
    button_GO = Button(Image("data/Кнопка.png"), k, k, buttons_sprites)
    button_GO.rect.x = X_BUTTON
    button_GO.rect.y = Y_BUTTON
    if buy_car:
        button_GO.set_text(button_GO_dct[buy_car])
    else:
        button_GO.set_text(button_GO_dct[buy_car].format(cars[index_car].specifications["Cost"]))

    recalculate_car = True

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if button_GO.rect.collidepoint(event.pos):
                    button_GO.change_picture(Image("data/Кнопка светлая.png"),
                                             button_GO.deafult_k_image_width,
                                             button_GO.deafult_k_image_height)
                else:
                    button_GO.set_deafult()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_GO.rect.collidepoint(event.pos):
                    if buy_car:
                        starter = Starter(main_game, screen, size, save, road, cars[index_car])
                        save.save()
                        return starter
                    else:
                        if cars[index_car].specifications["Cost"] <= save.specifications.money:
                            save.specifications.money -= cars[index_car].specifications["Cost"]
                            texts['you_counts'].value = [save.specifications.money]
                            save.specifications.name_cars.append(cars[index_car].info['name'])
                            recalculate_car = True
                if button_left.rect.collidepoint(event.pos) or button_right.rect.collidepoint(
                        event.pos):
                    if button_left.rect.collidepoint(event.pos):
                        index_car = (index_car - 1) % len(cars)
                        # print("button_left")
                    else:
                        index_car = (index_car + 1) % len(cars)
                        # print("button_right")
                        recalculate_car = True
        if recalculate_car:
            recalculate_car = False
            buy_car = cars[index_car].info["name"] in save.specifications.name_cars
            texts['message'].value = [dct_message['ok']]
            if buy_car:
                button_GO.set_text(button_GO_dct[buy_car])
            else:
                button_GO.set_text(
                    button_GO_dct[buy_car].format(cars[index_car].specifications["Cost"]))
        # Вывод
        screen.fill(pygame.Color((0, 0, 0)))
        background_sprites.draw(screen)
        screen.blit(cars[index_car].basic_image.image, cars[index_car].basic_image.rect)

        pygame.draw.rect(screen, (0, 0, 0), (
        X_TEXT_BEGIN, Y_BLOCK_BEGIN_TEXT, X_TEXT_END - X_TEXT_BEGIN,
        Y_BLOCK_END_TEXT - Y_BLOCK_BEGIN_TEXT))

        arrows_sprites.draw(screen)
        for i in texts:
            texts[i].render(screen)
        buttons_sprites.draw(screen)
        button_GO.render_text(screen)
        if not buy_car:
            clok_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
