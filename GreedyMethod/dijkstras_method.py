"""
Dijkstra's algorithm is suited to find the shortest path from a source to all other points

Finds shortest path to each vextex from a source vertex
"""
from typing import List

from constants.all_graph_matrices_to_copy import *


class Graph:
    def __init__(self, graph_matrix: List[List[int]]):
        self.v = len(graph_matrix)
        self.graph = graph_matrix


def find_shortest_path_on_vertex(in_vtx, in_g, shortest_path_to_vertices, visited_vertices):
    shortest_path = INF
    shortest_ind = 0
    for ind in range(in_g.v):
        edge = in_g.graph[in_vtx][ind]
        if 0 < edge < INF:
            if shortest_path_to_vertices[in_vtx] + edge < shortest_path_to_vertices[ind]:
                shortest_path_to_vertices[ind] = shortest_path_to_vertices[in_vtx] + edge

            if edge < shortest_path and not visited_vertices[ind]:
                shortest_path = in_g.graph[in_vtx][ind]
                shortest_ind = ind

    return shortest_ind


def dijkstras_method(in_g, src_vertex):
    shortest_path_to_vertices = [INF] * in_g.v
    visited_vertices_list = [False] * in_g.v
    shortest_path_to_vertices[src_vertex] = 0
    visited_vertices_count = 0
    while visited_vertices_count < in_g.v:
        shortest_ind = find_shortest_path_on_vertex(src_vertex, in_g, shortest_path_to_vertices,
                                                                   visited_vertices_list)

        visited_vertices_count += 1
        visited_vertices_list[src_vertex] = True
        src_vertex = shortest_ind

    print(shortest_path_to_vertices)

input_graph = Graph(GRAPH_3_DIRECTED)
dijkstras_method(input_graph, 0)

