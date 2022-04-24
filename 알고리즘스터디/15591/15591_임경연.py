

N, Q = map(int, input().split())

space = [[] for _ in range(N)]
answer = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N-1):
    a, b, l = map(int, input().split())
    space[a-1].append((b-1, l))
    space[b-1].append((a-1, l))

def DFS(node):
    visited = [0] * N
    visited[node] = 1
    stack = [[node, 1e12]]

    while stack:
        n, v = stack.pop()
        for i in range(len(space[n])):
            next_n, next_v = space[n][i]
            if visited[next_n] == 0:
                visited[next_n] = 1
                answer[node][next_n] = min(v, next_v)
                stack.append([next_n, min(v, next_v)])

for i in range(N):
    DFS(i)

counts = []

for i in range(Q):
    k, v = map(int, input().split())
    count = 0
    for j in answer[v-1]:
        if j >= k:
            count += 1
    counts.append(count)

for i in counts:
    print(i)


