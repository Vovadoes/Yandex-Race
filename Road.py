import math

import pygame

from Image import Image
from Mark import Locality
from functions import mark_conversion
from Dijkstra import dijkstra
import pickle


class Map(pygame.sprite.Sprite):
    save_path = r'./data/Maps/{}/{}'

    def __init__(self, image: Image, *group):
        self.name = None
        self.deafult_image = image
        self.image = image.image
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.start = Locality(238, 165)
        self.graph = None
        self.conversion_graph = None
        self.dct_points = None
        self.PX_KM = None  # Сколько пикселей в 1ом километре
        self.MONEY_KM = None  # колиство монет за 1 км

    def set_graph(self, graph):
        self.graph = graph
        self.dct_points, self.conversion_graph = mark_conversion(self.graph)

    def save(self, name=None):
        if name is None:
            name = self.name
        self.name = name
        pickle.dump(self.graph, open(self.save_path.format(name, 'graph.txt'), 'wb+'))
        pickle.dump(self.dct_points, open(self.save_path.format(name, 'dct_points.txt'), 'wb+'))
        pickle.dump(self.conversion_graph,
                    open(self.save_path.format(name, 'conversion_graph.txt'), 'wb+'))
        lst_const = [self.PX_KM, self.MONEY_KM]
        pickle.dump(lst_const, open(self.save_path.format(name, 'info.txt'), 'wb+'))

    def load(self, name=None):
        if name is None:
            name = self.name
        self.name = name
        self.graph = pickle.load(open(self.save_path.format(name, 'graph.txt'), 'rb'))
        self.dct_points = pickle.load(open(self.save_path.format(name, 'dct_points.txt'), 'rb'))
        self.conversion_graph = pickle.load(
            open(self.save_path.format(name, 'conversion_graph.txt'), 'rb'))
        self.PX_KM, self.MONEY_KM = pickle.load(open(self.save_path.format(name, 'info.txt'), 'rb'))


class Text:
    def __init__(self, text, x=0, y=0, height=10):
        self.text = text
        self.value = ['None']
        self.height = height
        self.x = x
        self.y = y

    def render(self, screen, color=(255, 204, 0)):
        font = pygame.font.Font(None, self.height)
        render = font.render(self.text + str(''.join([str(i) for i in self.value])), True, color)
        screen.blit(render, (self.x, self.y))

    def __str__(self):
        return self.text + str(''.join([str(i) for i in self.value]))


def distance(coords, coords_last):
    return math.sqrt(((coords[0] - coords_last[0]) ** 2) + ((coords[1] - coords_last[1]) ** 2))


class Road:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        self.way = None
        self.distance = None
        self.money = 0
        self.time = 60

    def find_way(self, graph):
        visited = dijkstra(self.start, self.finish, graph)

        lst = [self.finish]
        cur_node = self.finish
        # print(f'\npath from {self.finish} to {self.start}: \n {self.finish} ', end='')
        while cur_node != self.start:
            cur_node = visited[cur_node]
            lst.append(cur_node)
        #     print(f'---> {cur_node} ', end='')
        self.way = lst[::-1]
        return self.way

    def get_distance(self):
        self.distance = 0
        if len(self.way) != 0:
            coords_last = self.way[0].get_coords()
            for i in range(1, len(self.way)):
                coords = self.way[i].get_coords()
                self.distance += distance(coords, coords_last)
                coords_last = coords
        return self.distance
