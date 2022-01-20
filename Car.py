import json
import pickle
import os

from Button import Button
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
    info = {'name': 'None', 'path_basic_image': 'basic_image.png', 'path_images': 'images',
            'path_class_car': 'class_car.txt', 'path_mask': 'basic_image.png',
            'path_info': 'info.json', "path_specifications": "specifications.txt"}
    specifications = {"max_speed": 10, "boost": 10}

    def __init__(self, basic_image: Button = None, mask: Button = None, class_car: ClassCar = None):
        self.basic_image = basic_image
        self.images: list[Button] = []
        self.class_car: ClassCar = class_car
        self.mask: Button = mask
        # self.specifications = {"max_speed": 10, "boost": 10}

    def load(self, name):
        full_path = os.path.join(self.path_save, name)
        self.info = json.load(open(os.path.join(full_path, self.info['path_info']), 'rb'))
        self.basic_image = Button(Image(os.path.join(full_path, self.info["path_basic_image"])))
        for i in os.listdir(os.path.join(full_path, self.info['path_images'])):
            self.images.append(Button(Image(os.path.join(full_path, self.info['path_images'], i))))
        self.class_car = pickle.load(
            open(os.path.join(full_path, self.info["path_class_car"]), 'rb'))
        self.mask = Button(Image(os.path.join(full_path, self.info["path_mask"])))
        self.specifications = pickle.load(
            open(os.path.join(full_path, self.info["path_specifications"]), 'rb'))
        return self

    def save(self, name: str):
        self.info['name'] = name
        json.dump(self.info,
                  open(os.path.join(self.path_save, name, "info.json"), 'w+', encoding='UTF-8'),
                  default=json_util.default)
        pickle.dump(self.class_car,
                    open(os.path.join(self.path_save, name, self.info['path_class_car']), 'wb+'))
        pickle.dump(self.specifications,
                    open(os.path.join(self.path_save, name, self.info['path_specifications']),
                         'wb+'))
