import sys
INF = sys.maxsize
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
M = int(input())

# edgelist = []

# 초기화

W = [[INF for col in range(N+1)] for row in range(N+1)]

# 0 인덱스는 사용 안함


for i in range(1, N+1):
    # i,i 는 0
    W[i][i] = 0

for i in range(M):
    f_node, t_node = map(int, input().split())
    W[f_node][t_node] = 1

for i in range(N+1):
    for j in range(N+1):
        if(W[i][j] == -1):
            W[i][j] = sys.maxsize
            # 무한대 처리


#Floyd Warshall Start

#노드 by를 지날때 update
for by in range(1,N+1):
    for ffrom in range(1,N+1):
        for tto in range(1,N+1):
            # 노드 by를 이미 지난 것은 제외
            if(ffrom != by and tto != by):
                # 갱신
                if(W[ffrom][tto] > W[ffrom][by] + W[by][tto]):
                    W[ffrom][tto] = W[ffrom][by] + W[by][tto]

for a in range(1, N + 1):
    count = 0

    for b in range(1, N + 1):
        # 양쪽 모두 연결이 되지 않았을 경우 카운트
        if W[a][b] == INF and W[b][a] == INF:
            count += 1

    print(count)




