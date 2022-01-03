import pygame

from Mark import Mark
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

    marks = []

    mark = Mark(Image("Метка.png"), k_image_width, k_image_height, all_sprites)
    mark.centering(size[0], size[1])
    marks.append(mark)

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for mark in marks:
                    if mark.rect.collidepoint(event.pos):
                        mark.change_picture(Image("Метка активная.png"), k_image_width,
                                            k_image_height)
                        mark.centering(size[0], size[1])
                    else:
                        mark.set_deafult()
                        mark.centering(size[0], size[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)
        for mark in marks:
            mark.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
