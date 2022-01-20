import os.path
import datetime
import json
import pickle
from bson import json_util


class Specifications:
    def __init__(self, money=10):
        self.money = money


class Save:
    directory = './saves'

    def __init__(self, starter=None):
        self.starter = starter
        self.road_and_car = {}
        self.specifications = Specifications()
        self.info = {'date': datetime.datetime.now(), 'name': 'None', 'max_level_car': 0}

    def save(self, name: str):
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

        date = {'date': datetime.datetime.now()}
        if not os.path.exists(os.path.join(self.directory, 'info.json')):
            json.dump(self.info, open(os.path.join(self.directory, "info.json"), 'w+', encoding='UTF-8'),
                      default=json_util.default)

    def load(self, path):
        full_way = os.path.join(self.directory, path)
        self.info = json.load(open(os.path.join(full_way, "info.json"), 'r', encoding='UTF-8'))
        self.road_and_car = pickle.load(open(os.path.join(full_way, "road_and_car.txt"), 'rb+'))
        self.specifications = pickle.load(open(os.path.join(full_way, "specifications.txt"), 'rb+'))

    def set_last_save(self):
        lst = os.listdir(self.directory)
        full_way = os.path.join(self.directory)
        return None
