from collections import deque

def solution(board):
    answer = 1e10
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[1e10] * len(board) for _ in range(len(board))]

    queue = deque()
    visited[0][0] = 1
    queue.append([0, 0, 0, -1])

    while queue:
        v, x, y, d = queue.popleft()
        if x == len(board) - 1 and y == len(board) - 1 and (answer > v):
            answer = v
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if not (0 <= mx < len(board) and 0 <= my < len(board)) or board[my][mx] == 1:
                continue

            if d == -1 or d == i:
                cost = v + 100
            elif d != i:
                cost = v + 600

            if visited[my][mx] < cost - 400:
                continue
                        
            queue.append([cost, mx, my, i])
            visited[my][mx] = cost
    return answer