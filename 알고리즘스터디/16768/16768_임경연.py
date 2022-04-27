from collections import defaultdict
from copy import deepcopy

N, K = map(int, input().split())

maps = defaultdict(list)
# visited = [[] for _ in range(10)]

for i in range(N):
    inputs = list(map(int, input()))
    for j in range(len(inputs)):
        # visited[j] = [inputs[j]] + visited[j]
        if inputs[j] == 0:
            continue
        else:
            maps[j] = [inputs[j]] + maps[j]


move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS():
    visited = deepcopy(maps)
    token = 0
    del_idx = []

    while True:
        queue = []
        tmp_token = 0
        for i in range(10):
            for j in range(len(visited[i])):
                if visited[i][j] != 0:
                    queue.append([i, j])
                    tmp_token = 1
                    break
            if tmp_token == 1:
                break
        if tmp_token == 0:
            break

        tmp_del = []
        count = 1
        tmp_del.append([i, j])
        key = visited[i][j]
        visited[i][j] = 0
        
        while queue:
            x, y = queue.pop()
            
            
            for x_, y_ in move:
                m_x = x + x_
                m_y = y + y_

                if m_x < 0 or m_y < 0:
                    continue

                try:
                    if visited[m_x][m_y] != 0 and visited[m_x][m_y] == key:
                        queue.append([m_x, m_y])
                        tmp_del.append([m_x, m_y])
                        count += 1
                        visited[m_x][m_y] = 0
                except:
                    continue

        if count >= K:
            del_idx += tmp_del
            token = 1

    del_idx.sort(reverse=True)
    for x, y in del_idx:
        del maps[x][y]


    return token

while True:
    if DFS() == 0:
        break

answer = [[] for _ in range(N)]

for i in range(N):
    for j in range(10):
        if i >= len(maps[j]):
            answer[i].append(0)
        else:
            answer[i].append(maps[j][i])

for i in range(N):
    print("".join(list(map(str, answer[N - i - 1]))))


    






