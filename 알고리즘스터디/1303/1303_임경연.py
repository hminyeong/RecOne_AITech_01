import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []

visited = [[0] * N for _ in range(M)]
end_visited = [[1] * N for _ in range(M)]

for i in range(M):
    lst.append([i for i in input().split()[0]])


stack = [(0, 0)]
visited[0][0] = 1

w_answer = []
b_answer = []

cnt = 0
while True:

    if visited == end_visited and stack == []:
        if team == "W":
            w_answer.append(cnt**2)
        else:
            b_answer.append(cnt**2)
        break

    if stack == []:
        for i in range(M):
            for j in range(N):
                if visited[i][j] == 0:
                    stack.append((i, j))
                    visited[i][j] = 1
                    if team == "W":
                        w_answer.append(cnt**2)
                    else:
                        b_answer.append(cnt**2)
                    cnt = 0
                    break            
            if stack != []:
                break
    
    x, y = stack.pop()
    cnt += 1
    team = lst[x][y]

    possibleCrew = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

    for i, j in possibleCrew:
        if 0 <= i <= M-1 and 0 <= j <= N-1:
            if visited[i][j] == 0 and lst[i][j] == team:
                stack.append((i, j))
                visited[i][j] = 1

print(sum(w_answer), sum(b_answer))
