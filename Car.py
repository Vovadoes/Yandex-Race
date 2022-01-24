import json
import pickle
import os
from PIL import Image as Image_pil

from Button import Button
from Image import Image

from bson import json_util


class ClassCar:
    def __init__(self, name, k_money=1.0):
        self.name = name
        self.k_money = k_money

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return hash(self) == hash(other)


classes_car = [ClassCar("Первый"), ClassCar("Эконом", 1.2), ClassCar("Детский", 1.5),
               ClassCar("Бизнес", 2.1), ClassCar("Комфорт", 1.5), ClassCar("Премиум", 3),
               ClassCar("Быстрый", 2)]


class Car:
    path_save = "Cars"
    info = {'name': 'None', 'path_basic_image': 'basic_image.png', 'path_images': 'images',
            'path_class_car': 'class_car.txt', 'path_mask': 'basic_image.png',
            'path_info': 'info.json', "path_specifications": "specifications.json"}
    specifications = {"max_speed": 10, "boost": 10, 'Cost': 10}

    def __init__(self, basic_image: Button = None, mask: Button = None, class_car: ClassCar = None,
                 name: str = None):
        self.basic_image = basic_image
        self.images: list[Button] = []
        self.class_car: ClassCar = class_car
        self.mask: Button = mask
        # self.specifications = {"max_speed": 10, "boost": 10}

    def load(self, path):
        full_path = os.path.join(self.path_save, path)
        self.info = json.load(open(os.path.join(full_path, self.info['path_info']), 'rb'))
        self.basic_image = Button(Image(os.path.join(full_path, self.info["path_basic_image"])))
        for i in os.listdir(os.path.join(full_path, self.info['path_images'])):
            self.images.append(Button(Image(os.path.join(full_path, self.info['path_images'], i))))
        self.class_car = pickle.load(
            open(os.path.join(full_path, self.info["path_class_car"]), 'rb'))
        self.mask = Button(Image(os.path.join(full_path, self.info["path_mask"])))
        self.specifications = json.load(
            open(os.path.join(full_path, self.info["path_specifications"]), 'rb'))
        return self

    def save(self, name: str):
        self.info['name'] = name



        full_path = os.path.join(self.path_save, name, self.info["path_images"])

        if not os.path.exists(full_path):
            os.makedirs(full_path)
        for i in self.images:
            image = Image_pil.open(i.last_image.path)
            file_name = os.path.basename(i.last_image.path)
            image.save(os.path.join(full_path, file_name))

        full_path = os.path.join(self.path_save, name)

        self.info['path_basic_image'] = self.basic_image.last_image.path
        image = Image_pil.open(self.info['path_basic_image'])
        file_name = os.path.basename(self.info['path_basic_image'])
        self.info['path_basic_image'] = os.path.join(file_name)
        image.save(os.path.join(full_path, file_name))

        self.info['path_mask'] = self.mask.last_image.path
        image = Image_pil.open(self.info['path_mask'])
        file_name = os.path.basename(self.info['path_mask'])
        self.info['path_mask'] = os.path.join(file_name)
        image.save(os.path.join(full_path, file_name))

        json.dump(self.info,
                  open(os.path.join(full_path, "info.json"), 'w+', encoding='UTF-8'),
                  default=json_util.default)
        pickle.dump(self.class_car,
                    open(os.path.join(full_path, self.info['path_class_car']), 'wb+'))
        json.dump(self.specifications,
                  open(os.path.join(full_path, self.info["path_specifications"]), 'w+',
                       encoding='UTF-8'),
                  default=json_util.default)

    @staticmethod
    def get_class_car(path):
        full_path = os.path.join(Car.path_save, path)
        info = json.load(open(os.path.join(full_path, Car.info['path_info']), 'rb'))
        class_car = pickle.load(
            open(os.path.join(full_path, info["path_class_car"]), 'rb'))
        return class_car

