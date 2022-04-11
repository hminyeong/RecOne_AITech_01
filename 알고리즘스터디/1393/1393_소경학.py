xs, ys = map(int,input().split())
xe, ye, dx, dy = map(int,input().split())
if dx != 0 and dy != 0:
    for i in range(min(abs(dx),abs(dy)),0,-1):
        if abs(dx) % i == 0 and abs(dy) % i == 0:
            if dx >= 0:
                dx //= i
            else:
                dx = -abs(dx)//i
            if dy >= 0:
                dy //= i
            else:
                dy = -abs(dy)//i
            break
elif dx == 0:
    if dy > 0:
        dy = 1
    else:
        dy = -1
elif dy == 0:
    if dx > 0:
        dx = 1
    else:
        dx = -1
answer = 9999999
cnt = 0
x,y = 0,0
while True:
    if (xs-xe)**2 + (ys-ye)**2 < answer:
        answer = (xs-xe)**2 + (ys-ye)**2
        x = xe
        y = ye
    else:
        break
    xe += dx
    ye += dy
    
print(x,y)