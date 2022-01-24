import os.path
import datetime
import json
# import jsondatetime as json
import pickle
from bson import json_util

from Car import Car


class Specifications:
    def __init__(self, money=10, name_cars=None):
        if name_cars is None:
            name_cars = []
        self.money = money
        self.name_cars = name_cars


class Save:
    directory = 'saves'

    def __init__(self, car_def: Car = Car().load('first_car_r'), starter=None):
        self.starter = starter
        self.road_and_car = {}
        self.specifications = Specifications(10, [car_def.info["name"]])
        self.info = {'date': datetime.datetime.now(), 'name': 'None'}
        self.add_car(car_def)

    def add_car(self, car: Car):
        self.specifications.name_cars.append(car.info['name'])

    def save(self, name: str = None):
        if name is None:
            name = datetime.datetime.utcnow().replace(
                tzinfo=datetime.timezone.utc).isoformat().replace(':', '.')
        if self.info['name'] == "None":
            self.info['name'] = name
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        full_way = os.path.join(self.directory, self.info['name'])
        if not os.path.exists(full_way):
            os.makedirs(full_way)
        pickle.dump(self.road_and_car, open(os.path.join(full_way, "road_and_car.txt"), 'wb+'))
        json.dump(self.info, open(os.path.join(full_way, "info.json"), 'w+', encoding='UTF-8'),
                  default=json_util.default)
        pickle.dump(self.specifications, open(os.path.join(full_way, "specifications.txt"), 'wb+'))

        dct = {'date': datetime.datetime.now(), 'name': self.info["name"]}
        if not os.path.exists(os.path.join(self.directory, 'info.json')):
            json.dump(dct, open(os.path.join(self.directory, "info.json"), 'w+', encoding='UTF-8'),
                      default=json_util.default)
        else:
            date_old = json.load(
                open(os.path.join(self.directory, 'info.json'), 'r', encoding='UTF-8'),
                object_hook=json_util.object_hook)
            if dct['date'] > date_old["date"]:
                json.dump(dct,
                          open(os.path.join(self.directory, "info.json"), 'w+', encoding='UTF-8'),
                          default=json_util.default)

    def load(self, path):
        full_way = os.path.join(self.directory, path)
        self.info = json.load(open(os.path.join(full_way, "info.json"), 'r', encoding='UTF-8'),
                              object_hook=json_util.object_hook)
        self.road_and_car = pickle.load(open(os.path.join(full_way, "road_and_car.txt"), 'rb+'))
        self.specifications = pickle.load(open(os.path.join(full_way, "specifications.txt"), 'rb+'))

    def set_last_save(self):
        lst = os.listdir(self.directory)
        date = json.load(open(os.path.join(self.directory, 'info.json'), 'r', encoding='UTF-8'),
                         object_hook=json_util.object_hook)
        for name in lst:
            full_way = os.path.join(self.directory, name)
            if os.path.isdir(full_way):
                info = json.load(
                    open(os.path.join(full_way, "info.json"), 'r', encoding='UTF-8'),
                    object_hook=json_util.object_hook)
                if info["name"] == date["name"]:
                    return self.load(info["name"])

        return None

    @staticmethod
    def set_all_saves():
        saves = []
        full_way = ''
        lst = os.listdir(Save.directory)
        for i in lst:
            full_way = os.path.join(Save.directory, i)
            if os.path.isdir(full_way):
                info = json.load(open(os.path.join(full_way, "info.json"), 'r', encoding='UTF-8'),
                                 object_hook=json_util.object_hook)
                saves.append(info)
        saves.sort(key=lambda x: x['date'])
        return saves
