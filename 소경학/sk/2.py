def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    def first(n):
        if clockwise == True:
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
        else:
            dx = [1,0,-1,0]
            dy = [0,1,0,-1]
        s = 1
        i = 0
        start = n-1
        x,y = -dx[0],-dy[0]
        while start > 0:
            for j in range(start):
                x += dx[i]
                y += dy[i]
                answer[x][y] = s
                s += 1
            i = (i+1) % 4
            start -= 2 
    def second(n):
        if clockwise == True:
            dx = [1,0,-1,0]
            dy = [0,-1,0,1]
        else:
            dx = [0,1,0,-1]
            dy = [-1,0,1,0]
        s = 1
        i = 0
        start = n-1
        x,y = -dx[0],(n-1)-dy[0]
        while start > 0:
            for j in range(start):
                x += dx[i]
                y += dy[i]
                answer[x][y] = s
                s += 1
            i = (i+1) % 4
            start -= 2 
    def third(n):
        if clockwise == True:
            dx = [0,-1,0,1]
            dy = [-1,0,1,0]
        else:
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
        s = 1
        i = 0
        start = n-1
        x,y = (n-1)-dx[0],(n-1)-dy[0]
        while start > 0:
            for j in range(start):
                x += dx[i]
                y += dy[i]
                answer[x][y] = s
                s += 1
            i = (i+1) % 4
            start -= 2 
    def forth(n):
        if clockwise == True:
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
        else:
            dx = [0,-1,0,1]
            dy = [1,0,-1,0]
        s = 1
        i = 0
        start = n-1
        x,y = (n-1)-dx[0],-dy[0]
        while start > 0:
            for j in range(start):
                x += dx[i]
                y += dy[i]
                answer[x][y] = s
                s += 1
            i = (i+1) % 4
            start -= 2 
    
    first(n)
    second(n)
    third(n)
    forth(n)
    if n%2 == 1:
        answer[n//2][n//2] = n**2 // 4 + 1
    dic = {}
    for i in answer:
        for j in i:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
    print(dic)
    return answer