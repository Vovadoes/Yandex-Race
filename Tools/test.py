import math
from heapq import *
from pprint import pprint
from typing import Union

from Image import Image
from Mark import Crossroad, Locality
from Road import Map


def distance(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def mark_conversion(graph: dict[Union[Locality, Crossroad], Union[
    list[Crossroad], list[Union[Locality, Crossroad]], list[Locality]]]):
    dct1 = {}
    graph_new = {}

    for i in graph:
        if (i.x, i.y) not in dct1:
            dct1[(i.x, i.y)] = i
        graph_new[(i.x, i.y)] = []
        for j in graph[i]:
            graph_new[(i.x, i.y)].append((j.x, j.y))
            if (j.x, j.y) not in dct1:
                dct1[(j.x, j.y)] = j

    pprint(dct1)
    print()
    pprint(graph_new)
    graph = graph_new
    print()
    graph_new = {}

    for i in graph:
        if i not in graph_new:
            graph_new[i] = []
        for j in graph[i]:
            graph_new[i].append(j)
            if j not in graph_new:
                graph_new[j] = [i]
            else:
                graph_new[j].append(i)

    pprint(graph_new)
    print()
    graph = graph_new
    graph_new = {}

    for i in graph:
        if i not in graph_new:
            graph_new[i] = []
        for j in graph[i]:
            graph_new[i].append((distance(*i, *j), j))

    pprint(graph_new)
    print()
    graph = graph_new
    graph_new = {}

    for i in graph:
        if i not in graph_new:
            graph_new[dct1[i]] = []
        for j in graph[i]:
            graph_new[dct1[i]].append((j[0], dct1[j[1]]))

    pprint(graph_new)
    print()
    return dct1, graph_new


graph = {
    Locality(238, 165): [Crossroad(238, 284)],
    Crossroad(238, 284): [Crossroad(330, 284), Locality(161, 284)],
    Crossroad(330, 284): [Crossroad(330, 304)],
    Crossroad(330, 304): [Locality(330, 398), Locality(568, 304)],
    Locality(568, 304): [Locality(602, 304)],
    Locality(602, 304): [Crossroad(602, 353)],
    Locality(330, 398): [Crossroad(366, 398)],
    Crossroad(366, 398): [Locality(366, 448)],
    Locality(366, 448): [Crossroad(557, 448)],
    Crossroad(557, 448): [Locality(557, 646)],
    Locality(557, 646): [Crossroad(499, 646)],
    Crossroad(499, 646): [Crossroad(499, 663)],
    Crossroad(499, 663): [Crossroad(397, 663)],
    Crossroad(397, 663): [Locality(212, 663)],
    Locality(212, 663): [Crossroad(169, 663)],
    Crossroad(169, 663): [Crossroad(169, 678)],
    Crossroad(169, 678): [Locality(127, 678)],
    Locality(127, 678): [Crossroad(127, 441)],
    Crossroad(127, 441): [Crossroad(162, 441)],
    Crossroad(162, 441): [Locality(161, 284)]
}


def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited


def find_way():
    dct1, graph_new = mark_conversion(graph)
    start = dct1[(161, 284)]
    goal = dct1[(366, 440)]
    visited = dijkstra(start, goal, graph_new)

    cur_node = goal
    print(f'\npath from {goal} to {start}: \n {goal} ', end='')
    while cur_node != start:
        cur_node = visited[cur_node]
        print(f'---> {cur_node} ', end='')


image_map = Image("data/Maps/map1/map.jpg")
m = Map(image_map)
m.set_graph(graph)
m.specifications.PX_KM = 100
m.specifications.MONEY_KM = 10
m.save('map1')

# a = [1,2,34,45]
# print(a[:len(a):])
#
# print(round(2.5))
#
# a = Locality(12, 12)
# b = Locality(12, 12)
#
# print(hash(a), hash(b))
#
# print(a == b)
#
# dct = {a: []}
# print(dct[b])
