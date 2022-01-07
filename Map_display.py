import os

import pygame

from Button import Button
from Mark import Mark, Locality
from Save import Save
from functions import graph, mark_conversion, find_way
from Image import Image
from Road import Map, Road


def map_display(screen, size: tuple[int, int], save: Save):
    # создадим группу, содержащую все спрайты
    marks_sprites = pygame.sprite.Group()
    map_sprites = pygame.sprite.Group()

    image_map = Image(Map.save_path.format('map1', 'map.jpg'))
    maps = Map(image_map, map_sprites)

    k_image_width = size[0] / maps.image.get_width()
    k_image_height = size[1] / maps.image.get_height()

    maps.deafult_image.transform(size[0], size[1])
    maps.image = maps.deafult_image.image
    maps.load('map1')

    if len(save.road_and_car) == 0:
        start_point = maps.start
    else:
        start_point = save.road_and_car[-1].finish

    points = maps.dct_points

    way = []
    # road = Road(start_point, points[(366, 440)])

    # way = road.find_way(maps.conversion_graph)
    # print()
    # print(way)

    print(points)

    marks = []
    for tupl in points:
        if type(points[tupl]) is Locality:
            mark = Mark(button=Button(Image("Метка.png"), k_image_width, k_image_height, marks_sprites))
            mark.centering(points[tupl].get_coords(k_image_width, k_image_height))
            marks.append(mark)

    print(points[(366, 440)])

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
                        mark.centering()
                    else:
                        mark.button.set_deafult()
                        mark.centering()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for mark in marks:
                    if mark.button.rect.collidepoint(event.pos):
                        finish = mark.get_coords(1 / k_image_width, 1 / k_image_height)
                        finish = round(finish[0]), round(finish[1])
                        road = Road(start_point, points[finish])
                        way = road.find_way(maps.conversion_graph)
                        distance = road.get_distance()
                        print(f'{distance=}')
                        print(way)
                        break
        screen.fill(pygame.Color((0, 0, 0)))
        map_sprites.draw(screen)
        pygame.draw.circle(screen, (0, 0, 0), (size[0] - 350 * k_image_height * 0.5, 0),
                           350 * k_image_height)
        if len(way) != 0:
            coords_last = (way[0].x * k_image_width, way[0].y * k_image_height)
            for i in range(1, len(way)):
                coords = (way[i].x * k_image_width, way[i].y * k_image_height)
                pygame.draw.line(screen, (0, 0, 0), coords_last, coords, 5)
                coords_last = coords
        marks_sprites.draw(screen)
        for mark in marks:
            mark.button.render_text(screen)
        clock.tick(fps)
        pygame.display.flip()
    return None
