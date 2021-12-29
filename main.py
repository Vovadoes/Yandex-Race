import pygame
from functions import load_image
from Button import Button

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 450
    screen = pygame.display.set_mode(size)

    background = load_image("Фон меню.png")
    # button = load_image("Кнопка.png")

    k_image_width = width / background.get_width()
    k_image_height = height / background.get_height()

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    background_sprite = pygame.sprite.Sprite()
    # определим его вид
    background_sprite.image = pygame.transform.scale(background, size)
    # и размеры
    background_sprite.rect = background_sprite.image.get_rect()
    # добавим спрайт в группу
    all_sprites.add(background_sprite)

    # # создадим спрайт
    # button_sprite = pygame.sprite.Sprite()
    # # определим его вид
    # button_sprite.image = pygame.transform.scale(button, (int(button.get_width() * k_image_width), int(button.get_height() * k_image_height)))
    # # и размеры
    # button_sprite.rect = button_sprite.image.get_rect()
    # # добавим спрайт в группу
    # all_sprites.add(button_sprite)

    buttons = []
    button = Button("Кнопка.png", k_image_width, k_image_height, all_sprites)
    button.rect.x = 100
    button.rect.y = 100
    buttons.append(button)

    k = 20
    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if button.rect.collidepoint(event.pos):
                    button.change_picture("Кнопка светлая.png", k_image_width, k_image_height)
                else:
                    button.set_deafult()
                print(button.rect.collidepoint(event.pos))
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)

        clock.tick(fps)
        pygame.display.flip()
