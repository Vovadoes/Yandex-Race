from Button import Button


class Mark(Button):
    def centering(self, x, y):
        self.rect.x = x // 2 - self.rect.width // 2
        self.rect.y = y // 2 - self.rect.height
