import pygame
from Menu import menu
from Map_display import map_display
from Save import Save
from Starter import Starter


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    # starter = Starter(menu, screen, size)
    starter = Starter(map_display, screen=screen, size=size, save=Save())

    while True:
        starter = starter.start()
        if starter is None:
            break
        starter: Starter
