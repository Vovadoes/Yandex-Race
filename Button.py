import pygame
from Image import Image


class Button(pygame.sprite.Sprite):
    def __init__(self, image: Image, k_image_width=1, k_image_height=1, *group):
        self.deafult_k_image_width = k_image_width
        self.deafult_k_image_height = k_image_height
        self.deafult_image = image
        self.last_image = None
        self.change_picture(self.deafult_image, k_image_width, k_image_height, 0, 0)
        super().__init__(*group)
        self.text = None
        self.starter = None

    def change_picture(self, image: Image, k_image_width=1, k_image_height=1, x=None, y=None):
        if self.last_image is not None:
            if self.last_image == image:
                return None
        self.last_image = image
        if x is None:
            x = self.rect.x
        if y is None:
            y = self.rect.y
        self.image = pygame.transform.scale(self.last_image.image, (
            int(self.last_image.image.get_width() * k_image_width),
            int(self.last_image.image.get_height() * k_image_height)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def set_deafult(self):
        if self.last_image == self.deafult_image:
            return None
        self.change_picture(self.deafult_image, self.deafult_k_image_width,
                            self.deafult_k_image_height)
        self.last_image = self.deafult_image

    def set_text(self, text):
        self.text = text

    def render_text(self, screen, color=(255, 204, 0)):
        font = pygame.font.Font(None, self.rect.height)
        render = font.render(self.text, True, color)
        screen.blit(render, (self.rect.x, self.rect.y))
