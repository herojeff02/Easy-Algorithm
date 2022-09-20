
def isSafe(v, colour, c):
    for i in range(V):
        if graph[v][i] == 1 and colour[i] == c:
            return False
    return True

# A recursive utility function to solve m
# coloring  problem
def graphColourUtil(m, colour, v):
    if v == V:
        return True

    for c in range(1, m + 1):
        print(colour)
        if isSafe(v, colour, c):
            print(c)
            colour[v] = c
            if graphColourUtil(m, colour, v + 1):
                return True
            colour[v] = 0
        else:
            print("not " + str(c))
    return False

def graphColouring(m):
    colour = [0] * V
    if not graphColourUtil(m, colour, 0):
        return False

    # Print the solution
    print("Solution exist and Following are the assigned colours:")
    for c in colour:
        print(c, end=' ')
    return True


# Driver Code
V=4
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
graphColouring(m)