import pygame
from Menu import menu
from Starter import Starter


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 450
    screen = pygame.display.set_mode(size)

    starter = Starter(menu, screen, size)

    while True:
        starter = starter.start()
        if starter is None:
            break
        starter: Starter
