"""
Bellman Forst algorithm is suited to find the shortest path from a source to all other points and  suitable in
cases where there are negative edges.

Caveat: Doesnt work if there is a negative weight on the total edges of a cycle, if there is a cycle.
        negative weight cycle example :

Time Complexity --> O(n^3)
Finds shortest path to each vextex from a source vertex
"""
import copy
from typing import List

from constants.all_graph_matrices_to_copy import *


class Graph:
    def __init__(self, graph_matrix: List[List[int]]):
        self.v = len(graph_matrix)
        self.graph = graph_matrix


def find_shortest_path_to_vertex(cur_vtx, in_g, shortest_path_to_vertices):
    for ind in range(in_g.v):
        edge = in_g.graph[cur_vtx][ind]
        if edge < INF:
            if shortest_path_to_vertices[cur_vtx] + edge < shortest_path_to_vertices[ind]:
                shortest_path_to_vertices[ind] = shortest_path_to_vertices[cur_vtx] + edge


def shortest_path_map_changed(old_list: list, new_list: list) -> bool:
    if old_list == new_list:
        print("same found")
        return False
    else:
        return True


def bellman_ford_method(in_g, src_vertex):
    shortest_path_to_vertices = [INF] * in_g.v
    shortest_path_to_vertices[src_vertex] = 0
    last_shortest_path_to_vertices = []
    redoing_graph_count = 0

    while redoing_graph_count < in_g.v-1:
        for current_vertx in range(in_g.v):
            find_shortest_path_to_vertex(current_vertx, in_g, shortest_path_to_vertices)
        print(shortest_path_to_vertices)
        if not shortest_path_map_changed(last_shortest_path_to_vertices, shortest_path_to_vertices):
            break
        last_shortest_path_to_vertices = copy.deepcopy(shortest_path_to_vertices)

        redoing_graph_count += 1

    print(shortest_path_to_vertices)

input_graph = Graph(GRAPH_5_NEGATIVE)
bellman_ford_method(input_graph, 0)

