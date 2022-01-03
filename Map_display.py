import pygame

from Button import Button
from Save import Save
from functions import load_image
from Image import Image


def map_display(screen, size: tuple[int, int], save: Save):
    background = load_image("Map/map.jpg")

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

    buttons = []

    button = Button(Image("Метка.png"), k_image_width, k_image_height, all_sprites)
    button.rect.x = size[0] // 2 - button.rect.width // 2
    button.rect.y = size[1] // 2 - button.rect.height
    buttons.append(button)

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.change_picture(Image("Метка активная.png"), k_image_width, k_image_height)
                        button.rect.x = size[0] // 2 - button.rect.width // 2
                        button.rect.y = size[1] // 2 - button.rect.height
                    else:
                        button.set_deafult()
                        button.rect.x = size[0] // 2 - button.rect.width // 2
                        button.rect.y = size[1] // 2 - button.rect.height
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)
        for i in buttons:
            i.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
