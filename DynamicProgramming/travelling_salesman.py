from constants.all_graph_matrices_to_copy import *
from typing import List


class Graph:
    def __init__(self, graph_matrix: List[List[int]]):
        self.v = len(graph_matrix)
        self.graph = graph_matrix


def find_cheapest_path_to_remaining_vertices(in_g: Graph, remaining_vertices: list, src_vertex: int,
                                             current_vertex: int, path_taken: str) -> (int, str):
    if not remaining_vertices:
        return in_g.graph[current_vertex][src_vertex], "{}".format(src_vertex)

    cost_list = []
    path_list = []
    for next_vertex in remaining_vertices:
        next_remaining = remaining_vertices[:]
        next_remaining.pop(next_remaining.index(next_vertex))
        cost_of_next_vertex, cheapest_path = find_cheapest_path_to_remaining_vertices(in_g, next_remaining, src_vertex,
                                                                                      next_vertex, path_taken)
        cost_list.append(cost_of_next_vertex + in_g.graph[current_vertex][next_vertex])
        path_list.append(cheapest_path)

    min_cost = min(cost_list)
    cost_index = cost_list.index(min_cost)
    selected_vertex = remaining_vertices[cost_index]
    return min_cost, "{} <- {}".format(path_list[cost_index], selected_vertex)


def find_cheapest_path_for_graph(in_g: Graph, src_vertex: int):
    cost_of_all_nodes = [INF] * in_g.v
    cost_of_all_nodes[src_vertex] = 0
    remaining_vertices = [i for i in range(in_g.v)]
    remaining_vertices.pop(src_vertex)
    path_taken = ""

    cheapest_cost, cheapest_path = find_cheapest_path_to_remaining_vertices(in_g, remaining_vertices, src_vertex,
                                                                              src_vertex, path_taken)
    print(cheapest_cost, "{} <- {}".format(cheapest_path, src_vertex))


if __name__ == "__main__":
    in_g = Graph(GRAPH_4_DIRECTED)
    source = 0
    find_cheapest_path_for_graph(in_g, source)