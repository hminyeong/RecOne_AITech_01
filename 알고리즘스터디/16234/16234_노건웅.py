import sys
from collections import deque
input = sys.stdin.readline

n, L, R = map(int,input().rstrip().split())
matrix = [list(map(int,input().rstrip().split())) for _ in range(n)]

move = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0] * n for _ in range(n)]

def possibleMove(matrix,i,j):
    for x, y in move:
        dx = j + x
        dy = i + y
        if 0 <= dx < n and 0 <= dy < n :
            if visited[dy][dx] == 0 and L <= abs(matrix[i][j] - matrix[dy][dx]) <= R :
                return True

def bfs(matrix):
    count = 0
    q = deque()
    while True:
        q = deque()
        isMovement = False
        visited = [[0] * n for _ in range(n)]
        count += 1
        for i in range(n):
            for j in range(n):
                edges = []
                sums = 0 
                nums = 0
                if visited[i][j] == 0:
                    if possibleMove(matrix,i,j):
                        isMovement = True
                        visited[i][j] = 1
                        edges.append((i,j))
                        q.append((i,j))
                        sums += matrix[i][j]
                        nums += 1
                        while q :
                            r,c = q.popleft()
                            for x, y in move:
                                dx = x + c
                                dy = y + r
                                if 0 <= dx < n and 0 <= dy < n :
                                    result = abs(matrix[r][c] - matrix[dy][dx])
                                    if visited[dy][dx] == 0 and L <= result <= R :
                                        visited[dy][dx] = count
                                        q.append((dy,dx))
                                        edges.append((dy,dx))
                                        sums += matrix[dy][dx]
                                        nums += 1
                        for k,l in edges:
                            matrix[k][l] = sums // nums
                    else :
                        visited[i][j] = -1
        if not isMovement:
            count -= 1
            break
    return count

print(bfs(matrix))
