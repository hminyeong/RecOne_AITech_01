
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1 # a > b

for a in range(1,n+1): # 자기자신 -> 자기자신 0으로
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0


def floyd():
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if graph[a][b] == 1 or graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    return graph


floyd()

'''
#출력
for a in range(1,n+1):
    for b in range(1,n+1):
        print(graph[a][b],end = ' ')
    print()'''

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        #i->j로 갈 수 없고, j->i로 갈 수 없으면 무게를 비교할 수 없음
        if not graph[i][j] and not graph[j][i]: 
            cnt += 1
    print(cnt-1)
        
