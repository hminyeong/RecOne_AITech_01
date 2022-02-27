a = [0,0,0,0,0,0,0]
array = []
n,m,x,y,k = map(int,input().split())
for _ in range(n):
    array.append(list(map(int,input().split())))

s = list(map(int,input().split()))
for i in range(k):
    if s[i] == 1:
        nx = x
        ny = y+1
        if 0<=nx<n and 0<=ny<m:
            a_1 = a[1]
            a_2 = a[2]
            a_3 = a[3]
            a_4 = a[4]
            a_5 = a[5]
            a_6 = a[6]
            if array[nx][ny] == 0:
                array[nx][ny] = a[3]
                a[1] = a_4
                a[2] = a_2
                a[3] = a_1
                a[4] = a_6
                a[5] = a_5
                a[6] = a_3
            else:
                a[6] = array[nx][ny]
                array[nx][ny] = 0
                a[1] = a_4
                a[2] = a_2
                a[3] = a_1
                a[4] = a_6
                a[5] = a_5
            x = nx
            y = ny
            print(a[1])
    elif s[i] == 2:
        nx = x
        ny = y-1
        if 0<=nx<n and 0<=ny<m:
            a_1 = a[1]
            a_2 = a[2]
            a_3 = a[3]
            a_4 = a[4]
            a_5 = a[5]
            a_6 = a[6]
            if array[nx][ny] == 0:
                array[nx][ny] = a[4]
                a[1] = a_3
                a[2] = a_2
                a[3] = a_6
                a[4] = a_1
                a[5] = a_5
                a[6] = a_4
            else:
                a[6] = array[nx][ny]
                array[nx][ny] = 0
                a[1] = a_3
                a[2] = a_2
                a[3] = a_6
                a[4] = a_1
                a[5] = a_5
            x = nx
            y = ny
            print(a[1])
    elif s[i] == 3:
        nx = x-1
        ny = y
        if 0<=nx<n and 0<=ny<m:
            a_1 = a[1]
            a_2 = a[2]
            a_3 = a[3]
            a_4 = a[4]
            a_5 = a[5]
            a_6 = a[6]
            if array[nx][ny] == 0:
                array[nx][ny] = a[2]
                a[1] = a_5
                a[2] = a_1
                a[3] = a_3
                a[4] = a_4
                a[5] = a_6
                a[6] = a_2
            else:
                a[6] = array[nx][ny]
                array[nx][ny] = 0
                a[1] = a_5
                a[2] = a_1
                a[3] = a_3
                a[4] = a_4
                a[5] = a_6
            x = nx
            y = ny
            print(a[1])
    else:
        nx = x+1
        ny = y
        if 0<=nx<n and 0<=ny<m:
            a_1 = a[1]
            a_2 = a[2]
            a_3 = a[3]
            a_4 = a[4]
            a_5 = a[5]
            a_6 = a[6]
            if array[nx][ny] == 0:
                array[nx][ny] = a[5]
                a[1] = a_2
                a[2] = a_6
                a[3] = a_3
                a[4] = a_4
                a[5] = a_1
                a[6] = a_5
            else:
                a[6] = array[nx][ny]
                array[nx][ny] = 0
                a[1] = a_2
                a[2] = a_6
                a[3] = a_3
                a[4] = a_4
                a[5] = a_1
            x = nx
            y = ny
            print(a[1])