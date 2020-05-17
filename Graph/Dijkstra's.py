graph_weight = {'A': {'B': 4, 'C': 2},
                'B': {'C': 5, 'D': 10},
                'C': {'E': 3},
                'D': {'F': 11},
                'E': {'D': 4},
                'F': {}}

infinity = float("inf")
weights = {'B': 4,
           'C': 2,
           'D': infinity,
           'E': infinity,
           'F': infinity}

parents = {'B': 'A',
           'C': 'A',
           'D': None,
           'E': None,
           'F': None}
used = []


def find_min_weight_item(items):
    min_weight = infinity
    min_weight_item = None
    for i in items:
        weight = items[i]
        if weight < min_weight and i not in used:
            min_weight = weight
            min_weight_item = i
    return min_weight_item


def dijkstra(graph, weight_graph):
    item = find_min_weight_item(weight_graph)
    while item is not None:
        weight = weight_graph[item]
        neighbors = graph[item]
        for n in neighbors.keys():
            new_weight = weight + neighbors[n]
            if weight_graph[n] > new_weight:
                weight_graph[n] = new_weight
                parents[n] = item
        used.append(item)
        item = find_min_weight_item(weight_graph)
    return weight_graph


print(dijkstra(graph_weight, weights))
print(parents)
