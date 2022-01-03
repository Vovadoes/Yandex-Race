from Button import Button
from Image import Image


class Mark:
    def __init__(self, x: int = 0, y: int = 0, button: Button = None):
        self.x = x
        self.y = y
        self.button = button
        if button is not None:
            self.centering(self.x, self.y)

    def set_button(self, button: Button = None):
        self.button = button
        if button is not None:
            self.centering(self.x, self.y)

    def centering(self, x, y):
        self.x = x
        self.y = y
        self.button.rect.x = x // 2 - self.button.rect.width // 2
        self.button.rect.y = y // 2 - self.button.rect.height

    def get_coords(self) -> tuple[int, int]:
        return self.x, self.y


class Crossroad(Mark):
    def __repr__(self):
        return f'Crossroad({self.x}, {self.y})'


class Locality(Mark):
    def __repr__(self):
        return f'Locality({self.x}, {self.y})'
