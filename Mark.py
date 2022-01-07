from Button import Button
from Image import Image


class Mark:
    def __init__(self, x: int = 0, y: int = 0, button: Button = None):
        self.x = x
        self.y = y
        self.button = button
        if button is not None:
            self.centering((self.x, self.y))

    def set_button(self, button: Button = None):
        self.button = button
        if button is not None:
            self.centering((self.x, self.y))

    def centering(self, coords: tuple[int, int] = None):
        if coords is not None:
            self.x, self.y = coords
        self.button.rect.x = self.x - self.button.rect.width // 2
        self.button.rect.y = self.y - self.button.rect.height

    def get_coords(self, k_image_width=1, k_image_height=1) -> tuple[int, int]:
        return self.x * k_image_width, self.y * k_image_height

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return hash(self) == hash(other)


class Crossroad(Mark):
    def __repr__(self):
        return f'Crossroad({self.x}, {self.y})'


class Locality(Mark):
    def __repr__(self):
        return f'Locality({self.x}, {self.y})'
