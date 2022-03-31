a,b,c = map(int,input().split())

dic = {}

def DFS(z,x,v):
    if (z,x,v) in dic:
        return
    dic[(z,x,v)] = 1
    if z+v >= a:
        DFS(a,x,z+v-a)
    else:
        DFS(z+v,x,0)
    if x+v >= b:
        DFS(z,b,x+v-b)
    else:
        DFS(z,x+v,0)
    if z+v >= v:
        DFS(z+v-v,x,v)
    else:
        DFS(0,x,z+v)
    if z+x >= b:
        DFS(z+x-b,b,v)
    else:
        (0,z+x,v)
    if z+x >= a:
        DFS(a,z+x-a,v)
    else:
        DFS(z+x,0,v)
    if z+v >= c:
        DFS(z+v-c,x,c)
    else:
        DFS(0,x,z+v)
DFS(0,0,c)
answer = set()
for i in dic:
    if i[0] == 0:
        answer.add(i[2])
answer = list(answer)
answer.sort()
print(*answer)

