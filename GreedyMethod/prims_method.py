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


class Sol:
    def __init__(self):
        self.first_edge = True

    def find_most_min_cost_in_matrix(self, graph: List[List[int]], visited_nodes: List[bool]) -> (int, int, int):
        """
            Finds the minimum edge from a list of unselected edges
        Params :
        returns:
        """
        min_cost = float("inf")
        source = dest = 0
        for row in range(len(graph)):
            for col in range(len(graph[row])):
                edge = graph[row][col]
                if self.first_edge:
                    if edge != 0 and edge < min_cost:
                        min_cost, source, dest = edge, row, col
                else:
                    if edge != 0 and edge < min_cost and not(visited_nodes[row] and visited_nodes[col]) and (visited_nodes[row] or visited_nodes[col]):
                        min_cost, source, dest = edge, row, col
        if self.first_edge:
            self.first_edge = False
        print(min_cost, source, dest)
        return min_cost, source, dest


    def find_mcst_by_prims(self, pg: Graph):
        visited_node_count = 1
        minimum_cost_dict = dict()
        visited_node_vertices = [False] * pg.v
        while visited_node_count < pg.v:
            min_cost, source, dest = self.find_most_min_cost_in_matrix(pg.graph, visited_node_vertices)
            if not visited_node_vertices[source]:
                visited_node_vertices[source] = True
            if not visited_node_vertices[dest]:
                visited_node_vertices[dest] = True
            print(visited_node_vertices)
            visited_node_count += 1
            minimum_cost_dict["{}-{}".format(source, dest)] = min_cost

        print(minimum_cost_dict)


g = Graph(GRAPH_2)
solution = Sol()
solution.find_mcst_by_prims(g)
