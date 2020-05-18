import random
graph_undirected = {'A': {'B': 7, 'D': 5},
                    'B': {'A': 7, 'C': 8, 'E': 7},
                    'C': {'B': 8, 'E': 5},
                    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
                    'E': {'C': 5, 'B': 7, 'D': 15, 'F': 8, 'G': 9},
                    'F': {'D': 6, 'E': 8, 'G': 11},
                    'G': {'F': 11, 'E': 9}}
infinity = float("inf")
used = []


def search_min(graph, selected):
    min_weight = infinity
    min_weight_item = None
    neighbor = None
    for i in selected:
        for j in graph[i]:
            if j not in selected:
                weight = graph[i][j]
                if weight < min_weight:
                    neighbor = i
                    min_weight = weight
                    min_weight_item = j
    return [neighbor, min_weight_item, min_weight]


def prim(graph):
    unselected = [i for i in list(graph.keys())[1:]]
    selected = [list(graph.keys())[0]]
    result = {}
    for i in unselected:
        neighbor, min_weight_item, min_weight = search_min(graph, selected)
        if neighbor not in result:
            result[neighbor] = {}
        result[neighbor][min_weight_item] = min_weight
        if min_weight_item not in result:
            result[min_weight_item] = {}
        result[min_weight_item][neighbor] = min_weight
        selected.append(min_weight_item)

    return result


otv = prim(graph_undirected)

for item in otv.items():
    print(item)
