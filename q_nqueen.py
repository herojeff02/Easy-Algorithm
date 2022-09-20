def isSafe(row, col, diagID, r_diagID, rowLookup, diagLookup, r_diagLookup):
    return not (diagLookup[diagID[row][col]] or r_diagLookup[r_diagID[row][col]] or rowLookup[row])


def nqueenUtil(board, col, diagID, r_diagID, rowLookup, diagLookup, r_diagLookup):
    if col >= N:
        return True
    for i in range(N):
        if (isSafe(i, col, diagID, r_diagID, rowLookup, diagLookup, r_diagLookup)):
            board[i][col] = 1
            rowLookup[i] = True
            diagLookup[diagID[i][col]] = True
            r_diagLookup[r_diagID[i][col]] = True
            for j in range(N):
                for k in range(N):
                    print(board[j][k], end=" ")
                print()
            if nqueenUtil(board, col + 1, diagID, r_diagID, rowLookup, diagLookup, r_diagLookup):
                return True

            board[i][col] = 0
            rowLookup[i] = False
            diagLookup[diagID[i][col]] = False
            r_diagLookup[r_diagID[i][col]] = False

    return False

N = 4

board = [[0 for i in range(N)] for j in range(N)]
diagID = [[0 for i in range(N)] for j in range(N)]
r_diagID = [[0 for i in range(N)] for j in range(N)]
rowLookup = [False] * N
x = 2 * N - 1
diagLookup = [False] * x
r_diagLookup = [False] * x

for row in range(N):
    for col in range(N):
        diagID[row][col] = row + col
        r_diagID[row][col] = row - col + N - 1

if nqueenUtil(board, 0, diagID, r_diagID, rowLookup, diagLookup, r_diagLookup):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution")
