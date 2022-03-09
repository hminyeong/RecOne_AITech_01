n, a, b, c, d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0
def DFS(v,x,y,array,pb):
    global count
    if v == n:
        count += pb
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if [nx,ny] not in array:
            if i == 0:
                array.append([nx,ny])
                DFS(v+1,nx,ny,array,pb*(d/100))
                array.pop()
            elif i == 1:
                array.append([nx,ny])
                DFS(v+1,nx,ny,array,pb*(a/100))
                array.pop()
            elif i == 2:
                array.append([nx,ny])
                DFS(v+1,nx,ny,array,pb*(c/100))
                array.pop()
            elif i == 3:
                array.append([nx,ny])
                DFS(v+1,nx,ny,array,pb*(b/100))
                array.pop()
            

DFS(0,0,0,[[0,0]],1)
print(count)