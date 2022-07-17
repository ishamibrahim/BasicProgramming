"""
Prims algorithm is suited to find the minimum cost spanning tree (MCST).
MCST : is a graph with all vertices connected with the minimum cost edges

"""
from typing import List
from constants.all_graph_matrices_to_copy import *


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

# def def find_most_min_cost(vertex, graph: List[List[int]], visited_nodes: List[bool]) -> (int, int):
#     min_vertex = None
#     min_edge = 1000
#     for i in range(len(graph[vertex])):
#         edge = graph[vertex][i]
#         if edge != 0 and edge < min_edge and not visited_nodes[i]:
#             min_edge = edge
#             min_vertex = i
#     return (min_edge, min_vertex)
#
#
# def find_mcst_by_prims(pg: Graph):
#     visited_nodes_list = [False] * pg.v
#     visited_node_count = 1
#     minimum_cost_dict =dict()
#
#     vertex = 0
#     visited_nodes_list[vertex] = True
#     while visited_node_count < pg.v:
#         cost, next_vertex = find_most_min_cost(vertex, pg.graph, visited_nodes_list)
#         visited_nodes_list[next_vertex] = True
#         visited_node_count += 1
#         minimum_cost_dict["{0}-{1}".format(vertex, next_vertex)] = cost
#         vertex = next_vertex
#
#
#     print(minimum_cost_dict)


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
            if edge !=0 and edge < min_cost and not visited_nodes[row][col]:
                min_cost = edge
                source = row
                dest = col

    return min_cost, source, dest


def find_mcst_by_prims(pg: Graph):
    visited_node_count = 1
    minimum_cost_dict =dict()
    visited_nonde_matrix = [[False] * pg.v] * pg.v

    while visited_node_count < pg.v:
        min_cost, source, dest = find_most_min_cost_in_matrix(pg.graph, visited_nonde_matrix)
        visited_nonde_matrix [source][ dest] = True
        visited_nonde_matrix[dest][source] = True
        visited_node_count += 1
        minimum_cost_dict["{}-{}".format(source, dest)] = min_cost

    print(minimum_cost_dict)





selected = GRAPH_2
g = Graph(len(selected))
g.graph = selected

find_mcst_by_prims(g)