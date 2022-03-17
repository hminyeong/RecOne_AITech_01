import heapq
m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
array = []
visit = [[0] * m for i in range(n)]
for i in range(n):
    array.append(list(map(int, input())))
def BFS():
    q = []
    heapq.heappush(q, [0, 0, 0])
    visit[0][0] = 1
    while q:
        c, a, b = heapq.heappop(q)
        if a == n - 1 and b == m - 1:
            print(c)
            return
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
                heapq.heappush(q, [c + 1 if array[x][y] == 1 else c, x, y])
                visit[x][y] = 1
BFS()