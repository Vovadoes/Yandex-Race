import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Image:
    def __init__(self, path):
        self.image = load_image(path)
        self.path = path
        self.name = os.path.basename(path)

    def transform(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))

    def __eq__(self, other):
        return self.path == other.path

