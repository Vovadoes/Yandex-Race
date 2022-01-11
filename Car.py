import json
import pickle
import os

from Image import Image

from bson import json_util


class ClassCar:
    def __init__(self, name, k_money=1):
        self.name = name
        self.k_money = k_money


classes_car = []
classes_car.append(ClassCar("Обычный"))
classes_car.append(ClassCar("Премиум", 2))


class Car:
    path_save = "Cars"

    def __init__(self, basic_image: Image = None, mask: Image = None, class_car: ClassCar = None):
        self.basic_image = basic_image
        self.images: list[Image] = []
        self.class_car: ClassCar = class_car
        self.mask: Image = mask
        self.info = {'name': 'None', 'path_basic_image': 'basic_image.png', 'path_images': 'image/',
                     'path_class_car': 'class_car.txt', 'path_mask': 'basic_image.png'}

    def load(self):
        for i in os.listdir(os.path.join(self.path_save, self.info['path_images'])):
            self.images.append(Image(os.path.join(self.path_save, self.info['path_images'], i)))
        return self

    def save(self, name: str):
        self.info['name'] = name
        json.dump(self.info,
                  open(os.path.join(self.path_save, name, "info.json"), 'w+', encoding='UTF-8'),
                  default=json_util.default)
        pickle.dump(self.class_car,
                    open(os.path.join(self.path_save, name, self.info['path_class_car']), 'wb+'))
