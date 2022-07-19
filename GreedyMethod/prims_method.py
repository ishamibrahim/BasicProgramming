"""
Prims algorithm is suited to find the minimum cost spanning tree (MCST).
MCST : is a graph with all vertices connected with the minimum cost edges

"""
from typing import List
from constants.all_graph_matrices_to_copy import *


class Graph:
    def __init__(self, graph_matrix: List[List[int]]):
        self.v = len(graph_matrix)
        self.graph = graph_matrix


def find_most_min_cost_in_matrix(graph: List[List[int]], visited_nodes: List[List[int]]) -> (int, int, int):
    """

    Params :
    returns:
    """
    min_cost = float("inf")
    source = dest = 0
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            edge = graph[row][col]
            if edge != 0 and edge < min_cost and not visited_nodes[row][col]:
                min_cost = edge
                source = row
                dest = col

    return min_cost, source, dest


def create_visited_node_matrix(vertex_list: List[bool]):
    len_Vertex = len(vertex_list)
    visited_nonde_matrix = [[False] * len_Vertex] * len_Vertex
    for i in range(len_Vertex):
        if vertex_list[i]:
            for j in range(len_Vertex):
                if vertex_list[j]:
                    visited_nonde_matrix[i][j] = True
    return visited_nonde_matrix


def find_mcst_by_prims(pg: Graph):
    visited_node_count = 1
    minimum_cost_dict = dict()
    visited_nonde_vertices = [False] * pg.v
    visited_nonde_matrix = create_visited_node_matrix(visited_nonde_vertices)
    while visited_node_count < pg.v:
        min_cost, source, dest = find_most_min_cost_in_matrix(pg.graph, visited_nonde_matrix)
        if not visited_nonde_vertices[source]:
            visited_nonde_vertices[source] = True
        if not visited_nonde_vertices[dest]:
            visited_nonde_vertices[dest] = True
        visited_nonde_matrix = create_visited_node_matrix(visited_nonde_vertices)
        visited_node_count += 1
        minimum_cost_dict["{}-{}".format(source, dest)] = min_cost

    print(minimum_cost_dict)


g = Graph(GRAPH_2)
find_mcst_by_prims(g)
