import pickle

from MAIN_WINDOW import start_game
from Save import Save
import pygame
from Starter import Starter


if __name__ == '__main__':
    import Choosing_car
    from Menu import menu
    from Map_display import map_display



    pygame.init()
    size = width, height = 1542, 799
    screen = pygame.display.set_mode(size)
    s = pygame.mixer.Sound("data/c329a3c28705add.mp3")
    s.play(-1)


    starter = Starter(menu, screen, size)
    # starter = Starter(map_display, screen=screen, size=size, save=Save())
    # data = pickle.load(open('Tools/stat_save_road_car.txt', 'rb'))
    # starter = Starter(Choosing_car.choosing_car, screen, size, data[0], data[1])

    while True:
        starter = starter.start()
        if starter is None:
            break
        if starter.fn is start_game:
            s.stop()
        else:
            s.play(-1)
        starter: Starter
    s.stop()
