import pygame

from Image import Image
from Starter import Starter


def saves_dislpay(screen, size):
    from Menu import menu
    from Button import Button

    background_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    buttons_sprites = pygame.sprite.Group()

    background = Image('data/Фон выбора машины.png')

    # CONST
    k_image_width = size[0] / background.image.get_width()
    k_image_height = size[1] / background.image.get_height()
    k_image_standart = min(k_image_width, k_image_height)
    X_BUTTON_EXIT = int(0.02 * size[0])
    Y_BUTTON_EXIT = int(0.9 * size[1])

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

    img = Button(Image("data/Управление.png"), 1, 1)
    k = min(size[1] / img.rect.height,
            size[0] / img.rect.width)
    img = Button(img.deafult_image, k, k, all_sprites)
    img.rect.x = (size[0] - img.rect.width) // 2
    img.rect.y = (size[1] - img.rect.height) // 2

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
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)
        buttons_sprites.draw(screen)
        for i in buttons:
            i.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None