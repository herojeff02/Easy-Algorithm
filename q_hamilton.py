def isSafe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    for vertex in path:
        if vertex == v:
            return False
    return True


def hamCycleUtil(path, pos, V, graph):
    if pos == V:
        return graph[path[pos - 1]][path[0]] == 1
    for v in range(1, V):
        print(v)
        if isSafe(v, pos, path, graph):
            path[pos] = v
            if hamCycleUtil(path, pos + 1, V, graph):
                return True
            path[pos] = -1
    return False

def display(path):
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")


graph = [[0, 0, 1, 1],
         [0, 0, 1, 1],
         [1, 1, 0, 0],
         [1, 1, 0, 0]]
V=4
path = [-1] * V
path[0] = 0
if not hamCycleUtil(path, 1, V, graph):
    print("Solution does not exist\n")
else:
    display(path)