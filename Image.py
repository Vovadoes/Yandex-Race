from functions import load_image


class Image:
    def __init__(self, path):
        self.image = load_image(path)
        self.path = path

    def __eq__(self, other):
        return self.path == other.path