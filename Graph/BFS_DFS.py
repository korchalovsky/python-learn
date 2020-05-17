from _collections import deque

graph_directed = {'A': ['C', 'B'],
                  'B': ['A', 'D', 'E'],
                  'C': ['A', 'F'],
                  'D': ['B'],
                  'E': ['B', 'F'],
                  'F': ['C', 'E']}

graph_undirected = {1: [2, 3],
                    2: [4, 6],
                    3: [6],
                    4: [12],
                    6: [12],
                    12: []}


def bfs(graph_n, elem):
    queue = deque(graph_n[elem])
    visited = [elem]
    while queue:
        point = queue.popleft()
        if point not in visited:
            visited.append(point)
            queue += graph_n[point]
    return visited


def dfs(graph_n, elem):
    visited = [elem]
    stack = (graph_n[elem])
    while stack:
        point = stack.pop()
        if point not in visited:
            visited.append(point)
            stack += graph_n[point]
    return visited


print(bfs(graph_directed, 'A'))
print(bfs(graph_undirected, 1))

print(dfs(graph_directed, 'A'))
print(dfs(graph_undirected, 1))
