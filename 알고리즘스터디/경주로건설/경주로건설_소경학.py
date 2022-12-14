import sys
from collections import deque
 
 
def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    visit = [[sys.maxsize] * len(board) for _ in range(len(board))]
    visit[0][0] = 0
 
    q.append([0, 0, 0, 0])
 
    while q:
 
        x, y, state, cnt = q.popleft()
 
        for i in range(4):
 
            nx = x + dx[i]
            ny = y + dy[i]
 
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue
 
            if board[nx][ny] != 1:
                if (state == 1 and (i == 2 or i == 3)) or (state == 2 and (i == 0 or i == 1)):
                    if visit[nx][ny] >= cnt + 100:
                        if state == 1:
                            q.append([nx, ny, 1, cnt + 100])
                            visit[nx][ny] = cnt + 100
                        else:
                            q.append([nx, ny, 2, cnt + 100])
                            visit[nx][ny] = cnt + 100
                elif (state == 1 and (i == 0 or i == 1)) or (state == 2 and (i == 2 or i == 3)):
                    if visit[nx][ny] >= cnt + 600:
                        if state == 1:
                            q.append([nx, ny, 2, cnt + 600])
                            visit[nx][ny] = cnt + 600
                        else:
                            q.append([nx, ny, 1, cnt + 600])
                            visit[nx][ny] = cnt + 600
 

                else:
                    if i == 0 or i == 1:
                        q.append([nx, ny, 2, 100])
                        visit[nx][ny] = 100
                    else:
                        q.append([nx, ny, 1, 100])
                        visit[nx][ny] = 100
 
    return visit[len(board) - 1][len(board) - 1]