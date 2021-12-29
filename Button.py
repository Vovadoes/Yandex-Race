import pygame
from functions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, path, k_image_width=1, k_image_height=1, *group):
        self.deafult_path = path
        self.deafult_k_image_width = k_image_width
        self.deafult_k_image_height = k_image_height
        self.change_picture(path, k_image_width, k_image_height, 0, 0)
        super().__init__(*group)

    def change_picture(self, path, k_image_width=1, k_image_height=1, x=None, y=None):
        button = load_image(path)
        if x is None:
            x = self.rect.x
        if y is None:
            y = self.rect.y
        self.image = pygame.transform.scale(button, (
            int(button.get_width() * k_image_width), int(button.get_height() * k_image_height)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


    def set_deafult(self):
        self.change_picture(self.deafult_path, self.deafult_k_image_width,
                            self.deafult_k_image_height)
