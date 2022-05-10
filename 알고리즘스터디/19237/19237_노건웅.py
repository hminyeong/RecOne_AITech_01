import sys
def input(): return sys.stdin.readline().rstrip()

# [주의점]
# 1. 상어는 자신이 있는 곳에 냄새를 뿌린다.
#   1.1. K번 이동해야 냄새가 없어진다 => 즉, 이동 후 감소시켜야한다
# 2. 상어는 상하좌우로 움직일 수 있다
#   2.1. 아무 냄새가 없는 칸을 먼저
#   2.2. 그 다음은 자신의 냄새가 있는 칸의 방향으로
#   2.3. 가능한 곳이 여러 곳일 때는 우선순위대로
# 3. 1칸에는 1마리의 상어만 존재할 수 있다
#   3.1. 여러마리가 있을 경우 번호가 가장 작은 상어만 살아남는다.
# 4. 1000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
#   4.1. 1000초를 포함한다는 뜻 (즉, 1000번 이동까지는 허용)

def bfs(smell):
    moved = {}
    q = {}
    for s in range(1,m+1):
        if s not in shark: continue
        y,x,d = shark[s]
        ny,nx,nd = -1,-1,-1
        for move_d in shark_move[s][d]:
            dy, dx = y + my[move_d], x + mx[move_d]
            if 0 <= dy < n and 0 <= dx < n:
                if not visited[dy][dx]:
                    ny,nx,nd = dy,dx,move_d
                    break
        if ny == -1:
            for move_d in shark_move[s][d]:
                dy, dx = y + my[move_d], x + mx[move_d]
                if 0 <= dy < n and 0 <= dx < n:
                    if visited[dy][dx] == s:
                        ny,nx,nd = dy,dx,move_d
                        break
        if (ny,nx) not in moved:
            moved[(ny,nx)] = s
            shark[s] = (ny,nx,nd)
        else:
            del shark[s]
    for i,j in smell:
        if smell[(i,j)] > 1:
            q[(i,j)] = smell[(i,j)] - 1
        else:
            visited[i][j] = 0
    for i,j in moved:
        q[(i,j)] = K
        visited[i][j] = moved[(i,j)]
    return q

n,m,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
direction = [0] + list(map(int,input().split()))
shark_move = {i:{ j:list(map(int,input().split())) for j in range(1,5)} for i in range(1,m+1)}
shark = {}
visited = [[0] * n for _ in range(n)]
my = {1:-1,2:1,3:0,4:0}
mx = {1:0,2:0,3:-1,4:1}
smell = {}
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            shark[matrix[i][j]] = (i,j,direction[matrix[i][j]])
            visited[i][j] = matrix[i][j]
            smell[(i,j)] = K
            
possible = False
for c in range(1001):
    if len(shark) == 1:
        possible = True
        print(c)
        break
    smell = bfs(smell)
if not possible:
    print(-1)
