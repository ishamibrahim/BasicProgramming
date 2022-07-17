INF = float("inf")

# GRAPH_1_USUAL file : constants/graph_1_usual.jpeg
GRAPH_1_USUAL = [
    [   0,   2,   4, INF, INF, INF],
    [   2,   0,   1,   7, INF, INF],
    [   4,   1,   0, INF,   3, INF],
    [ INF,   7, INF,   0,   2,   1],
    [ INF, INF,   3,   2,   0,   5],
    [ INF, INF, INF,   1,   5,   0]
]

# GRAPH_1_UNUSUAL file : constants/graph_1_unusual.jpeg
GRAPH_1_UNUSUAL = [
    [   0, INF, INF,   4,   2, INF],
    [ INF,   0,   1, INF, INF,   5],
    [ INF,   1,   0, INF,   7,   2],
    [   4, INF, INF,   0,   1,   3],
    [   2, INF,   7,   1,   0, INF],
    [ INF,   5,   2,   3, INF,   0]
]

# GRAPH_2 file : constants/graph_2.jpeg
GRAPH_2 = [
    [   0,   2, INF,   6, INF],
    [   2,   0,   3,   8,   5],
    [ INF,   3,   0, INF,   7],
    [   6,   8, INF,   0,   9],
    [ INF,   5,   7,   9,   0]
]


# GRAPH_1_UNUSUAL file : constants/graph_3_directed.jpeg
GRAPH_3_DIRECTED = [
    [   0, 50, 45,   10,   INF, INF],
    [ INF,   0,   10, 15, INF,   INF],
    [ INF,   INF,   0, INF,   30,   INF],
    [   INF, INF, INF,   0,   15,   INF],
    [   INF, 20,   35,   INF,   0, INF],
    [ INF,   INF,   INF,   INF, 3,   0]
]
# GRAPH_1_UNUSUAL file : constants/graph_4_directed.jpeg
GRAPH_4_DIRECTED = [
    [0, 10, 15, 20],
    [5,  0,  9, 10],
    [6, 13,  0, 12],
    [8,  8,  9,  0]
]