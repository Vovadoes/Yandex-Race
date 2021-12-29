import pygame
from functions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, path, k_image_width=1, k_image_height=1, *group):
        self.change_picture(path, k_image_width, k_image_height)
        super().__init__(*group)

    def change_picture(self, path, k_image_width=1, k_image_height=1):
        button = load_image(path)
        self.image = pygame.transform.scale(button, (
            int(button.get_width() * k_image_width), int(button.get_height() * k_image_height)))
        self.rect = self.image.get_rect()
