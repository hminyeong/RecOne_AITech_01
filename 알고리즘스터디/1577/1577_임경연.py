import sys
from collections import deque


input = sys.stdin.readline

W, H = map(int, input().split())
K = int(input())

road = [[0] * (W + 1) for _ in range(H + 1)]

R_w = deque()
R_h = deque()

for i in range(K):
    a, b, c, d = map(int, input().split())
    if a == c: # 세로
        R_h.append((a, max(b, d)))
    else: # 가로
        R_w.append((max(a, c), b))



# 1번째 행 확인

r = W + 1

for i in range(len(R_w)):
    if R_w[i][1] == 0:
        r = min(r, R_w[i][0])
        

for i in range(r):
    road[0][i] = 1

# 2 ~ H번쨰 행 확인

for h in range(1, H + 1):
    A = []
    B = []
    for i in range(len(R_w)): # 가로
        if R_w[i][1] == h:
            A.append(R_w[i][0])
    for i in range(len(R_h)): # 세로
        if R_h[i][1] == h:
            B.append(R_h[i][0])

    for w in range(W + 1):
        if w == 0:
            if 0 not in B:
                road[h][w] = road[h-1][w]
        else:
            if w not in A and w not in B:
                road[h][w] = road[h][w - 1] + road[h - 1][w]
            elif w in A and w not in B:
                road[h][w] = road[h - 1][w]
                
            elif w not in A and w in B:
                road[h][w] = road[h][w - 1]

            else:
                continue
print(road[-1][-1])

