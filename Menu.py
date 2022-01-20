import pygame

from Button import Button
from Save import Save
from Starter import Starter
from Map_display import map_display
from Image import Image, load_image


def menu(screen, size):
    # Константы для окна
    heading_percentages = 10
    heading_xp = size[1] // (100 / heading_percentages)
    buttons_xp = size[1] - heading_xp

    background = load_image("data/Фон меню.png")

    k_image_width = size[0] / background.get_width()
    k_image_height = size[1] / background.get_height()

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(all_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    # инициализация кнопок
    buttons = []

    button = Button(Image("data/Кнопка.png"), k_image_width, k_image_height, all_sprites)
    button.set_text("Новая игра")
    save = Save()
    button.starter = Starter(map_display, save=save, size=size, screen=screen)
    buttons.append(button)

    button = Button(Image("data/Кнопка.png"), k_image_width, k_image_height, all_sprites)
    save = Save()
    save.save("first")
    save.load("first")
    button.starter = Starter(map_display, save=save, size=size, screen=screen)
    button.set_text("Продолжить")
    buttons.append(button)

    button = Button(Image("data/Кнопка.png"), k_image_width, k_image_height, all_sprites)
    button.set_text("Сохранения")
    buttons.append(button)

    button = Button(Image("data/Кнопка.png"), k_image_width, k_image_height, all_sprites)
    button.set_text("Настройки")
    buttons.append(button)

    button = Button(Image("data/Кнопка.png"), k_image_width, k_image_height, all_sprites)
    button.set_text("Выйти")
    button.starter = Starter(lambda: None)
    buttons.append(button)

    del button

    # Размещение на экране
    l = len(buttons)
    r = (buttons_xp - sum([i.rect.height for i in buttons])) / (l + 1)
    x = heading_xp + r
    for i in range(l):
        buttons[i].rect.x = (size[0] - buttons[i].rect.width) // 2
        buttons[i].rect.y = x
        x += r + buttons[i].rect.height

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
                        button.change_picture(Image("data/Кнопка светлая.png"), k_image_width, k_image_height)
                    else:
                        button.set_deafult()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.starter is not None:
                            return button.starter
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)
        for i in buttons:
            i.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
