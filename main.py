import pickle

from MAIN_WINDOW import start_game
from Save import Save
import pygame

from Starter import Starter

if __name__ == '__main__':
    from Saves_display import saves_dislpay
    import Choosing_car
    from Menu import menu
    from Map_display import map_display

    pygame.init()
    size = width, height = 1542, 799
    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load("data/c329a3c28705add.mp3")
    pygame.mixer.music.play(-1)
    starter = Starter(menu, screen, size)
    # starter = Starter(map_display, screen=screen, size=size, save=Save())
    # starter = Starter(saves_dislpay, screen=screen, size=size)
    # data = pickle.load(open('Tools/stat_save_road_car.txt', 'rb'))
    # starter = Starter(Choosing_car.choosing_car, screen, size, data[0], data[1])

    while True:
        if starter is None:
            break
        if starter.fn is start_game:
            # pygame.mixer.music.pause()
            pass
        else:
            # pygame.mixer.music.unpause()
            pass
        starter = starter.start()
        starter: Starter
    pygame.mixer.music.pause()
