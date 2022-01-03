import pygame

from Button import Button
from Mark import Mark
from Save import Save
from functions import graph, mark_conversion, find_way
from Image import Image
from Road import Map


def map_display(screen, size: tuple[int, int], save: Save):
    image_map = Image("Map1/map.jpg")

    k_image_width = size[0] / image_map.image.get_width()
    k_image_height = size[1] / image_map.image.get_height()

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    image_map.transform(size[0], size[1])
    maps = Map(image_map, all_sprites)

    marks = []

    mark = Mark(button=Button(Image("Метка.png"), k_image_width, k_image_height, all_sprites))
    mark.centering(size[0], size[1])
    marks.append(mark)

    global graph

    dct, graph_new = mark_conversion(graph)
    lst = find_way(dct[(161, 284)], dct[(366, 440)], graph_new)

    print(lst)

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                for mark in marks:
                    if mark.button.rect.collidepoint(event.pos):
                        mark.button.change_picture(Image("Метка активная.png"), k_image_width,
                                                   k_image_height)
                        mark.centering(size[0], size[1])
                    else:
                        mark.button.set_deafult()
                        mark.centering(size[0], size[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill(pygame.Color((0, 0, 0)))
        all_sprites.draw(screen)
        for mark in marks:
            mark.button.render_text(screen)
        if len(lst) != 0:
            coords_last = (lst[0].x * k_image_width, lst[0].y* k_image_height)
            for i in range(1, len(lst)):
                coords = (lst[i].x * k_image_width, lst[i].y * k_image_height)
                pygame.draw.line(screen, (0, 0, 0), coords_last, coords, 5)
                coords_last = coords
        clock.tick(fps)
        pygame.display.flip()
    return None
