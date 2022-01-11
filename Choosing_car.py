import pygame

from Road import Road
from Save import Save


def choosing_car(screen, size: tuple[int, int], save: Save, road: Road):

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill(pygame.Color((0, 0, 0)))
        clock.tick(fps)
        pygame.display.flip()
    return None
