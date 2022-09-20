import math

MAX = float('inf')


def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]


def firstMin(adj, i):
    min = MAX
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min


def secondMin(adj, i):
    first, second = MAX, MAX
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif (adj[i][j] <= second and
              adj[i][j] != first):
            second = adj[i][j]
    return second


def TSPUtil(curr_bound, curr_weight, level, curr_path, visited):
    print(curr_bound, curr_weight, level, curr_path, visited)
    global final_res
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            print(curr_path, curr_res)
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return
    for i in range(N):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPUtil(curr_bound, curr_weight, level + 1, curr_path, visited)
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True


adj = [[0, 4, 1, 1],
       [4, 0, 1, 1],
       [1, 1, 0, 4],
       [1, 1, 4, 0]]
N = 4

final_path = [None] * (N + 1)
final_res = MAX
curr_bound = 0
curr_path = [-1] * (N + 1)
visited = [False] * N
for i in range(N):
    curr_bound += (firstMin(adj, i) + secondMin(adj, i))
curr_bound = math.ceil(curr_bound / 2)
visited[0] = True
curr_path[0] = 0
TSPUtil(curr_bound, 0, 1, curr_path, visited)
print("Minimum cost :", final_res)
print("Path Taken : ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')
