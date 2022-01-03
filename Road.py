import pygame

from Image import Image


class Map(pygame.sprite.Sprite):
    save_path = r'./data/Map1'

    def __init__(self, image: Image, *group):
        self.deafult_image = image
        self.image = image.image
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.starter = None


class Road:
    def __init__(self):
        pass



