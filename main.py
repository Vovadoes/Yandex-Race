import pickle

import pygame

# import Choosing_car
# from Menu import menu
from Map_display import map_display
from Save import Save
from Starter import Starter

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1542, 799
    screen = pygame.display.set_mode(size)

    starter = Starter(menu, screen, size)
    # starter = Starter(map_display, screen=screen, size=size, save=Save())
    # data = pickle.load(open('Tools/stat_save_road_car.txt', 'rb'))
    # starter = Starter(Choosing_car.choosing_car, screen, size, data[0], data[1])

    while True:
        starter = starter.start()
        if starter is None:
            break
        starter: Starter
