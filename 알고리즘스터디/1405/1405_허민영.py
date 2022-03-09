import sys
input = sys.stdin.readline

N, e,w,s,n = map(int, input().split())

percent = [e/100, w/100, s/100, n/100]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph = [[0]*(2*N+1) for _ in range(2*N+1)]

total = 0

def dfs(x, y, p, count): # 미친로봇의 시작 지점, 최초 확률 1, 횟수
    global total
    if count == N: # 겹치지 않고 N번 만큼 돌았으면
        total += p
        return

    P = p # 동서남북 확률값
    graph[x][y] = 1 # 현재 좌표 방문 처리
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x <= -1 or new_x >= 2*N+1 or new_y <= -1 or new_y >= 2*N+1:
            return False
        else:
            if graph[new_x][new_y] == 1: # 방문했던 곳이면
                continue
            else: # 방문 안했을 경우
                dfs(new_x,new_y, P*percent[i], count+1) # 재귀
        graph[new_x][new_y] = 0 # 다음 탐색을 위해서
    return total
    

dfs(N, N, 1, 0)

print(total)


