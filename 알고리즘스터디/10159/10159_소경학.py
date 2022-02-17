import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
array = [[[],[]] for _ in range(n+1)]
for _ in range(m):
    l, h = map(int,input().split())
    array[l][1].append(h)
    array[h][0].append(l)
visit = [False for _ in range(n+1)]

def find_back(node):
    for i in array[node][1]:
        if visit[i] == False:
            visit[i] = True
            find_back(i)
def find_front(node):
    for i in array[node][0]:
        if visit[i] == False:
            visit[i] = True
            find_front(i)

for i in range(1,n+1):
    visit=[False for _ in range(n+1)]
    visit[0], visit[i] = True, True
    find_back(i)
    find_front(i)
    print(visit.count(False))
