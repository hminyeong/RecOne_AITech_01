import sys
from collections import deque

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

def solution(board):
    N = len(board)
    arr = [[[sys.maxsize]*4 for _ in range(N)] for _ in range(N)]
    queue = deque()

    queue.append([0, 0, -1])
    arr[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, direction = queue.popleft()
        for i in range(4):
            if i + direction == 3:
                continue
            nx = x+dx[i]
            ny = y+dy[i]
            cost = 100
            if i != direction and direction != -1:
                cost += 500
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and arr[nx][ny][i] > cost+arr[x][y][direction]
                arr[nx][ny][i] = cost+arr[x][y][direction]
                queue.append([nx, ny, i])

    return min(arr[N-1][N-1])
