import pygame

from Image import load_image, Image
from Starter import Starter


def control(screen, size):
    from Menu import menu
    # Константы для окна

    background = load_image("data/Фон меню.png")

    k_image_width = size[0] / background.get_width()
    k_image_height = size[1] / background.get_height()

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    buttons_sprites = pygame.sprite.Group()

    X_BUTTON_EXIT = int(0.02 * size[0])
    Y_BUTTON_EXIT = int(0.9 * size[1])


    # создадим спрайт
    background_sprite = pygame.sprite.Sprite(all_sprites)
    # определим его вид
    background_sprite.image = pygame.transform.scale(background, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()

    buttons = []

    from Button import Button
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
                        button.change_picture(Image("data/Кнопка светлая.png"), button.deafult_k_image_width,
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