
N, L, R = map(int, input().split())

space = []

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    space.append(list(map(int, input().split())))

def DFS():
    visited = [0] * (N**2)
    token = 0

    while 0 in visited:
        c = 0
        p = 0
        q = []
        y, x = visited.index(0)//N, visited.index(0)%N
        
        visited[y*N + x] = 1
        q.append([y, x])
        c += 1
        p += space[y][x]
        locs = [[y, x]]
        while q:
            y, x = q.pop()
            for m_y, m_x in move:
                y_ = y + m_y
                x_ = x + m_x
                if 0 <= y_ < N and 0 <= x_ < N and visited[y_ * N + x_] == 0:
                    if L <= abs(space[y][x] - space[y_][x_]) <= R:
                        visited[y_ * N + x_] = 1
                        q.append([y_, x_])
                        c += 1
                        p += space[y_][x_]
                        locs.append([y_, x_])
        if len(locs) >= 2:
            token = 1
            v = p // c
            for y, x in locs:
                space[y][x] = v
    return token

answer = 0
while True:
    token = DFS()
    if token == 0:
        break
    else:
        answer += 1

print(answer)

