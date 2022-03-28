def DFS(v):
    for i in array[v]:
        if visit[i] == True:
            total[0] = 1
        visit[i] = True
        DFS(i)
time = 0
while True:
    time += 1
    c = set()
    array = [[] for _ in range(100)]
    b = set()
    visit = [22 for _ in range(100)]
    total = [0]
    real_check = False
    while True:
        a = list(map(int,input().split()))
        check = False
        for i in range(0,len(a),2):
            if a[i] == 0 and a[i+1] == 0:
                check = True
                break
            if a[i] == -1 and a[i+1] == -1:
                real_check = True
                break
            if a[i] == a[i+1]:
                total[0] = 1
            visit[a[i]] = False
            visit[a[i+1]] = False
            c.add(a[i])
            c.add(a[i+1])
            b.add(a[i+1])
            array[a[i]].append(a[i+1])
        if check == True or real_check == True:
            break
    if real_check == True:
        break
    root = -5
    count = 0
    for i in c:
        if i not in b:
            root = i
            count += 1
            if count == 2:
                total[0] = 1
                break
    visit[root] = True
    DFS(root)
    if total[0] == 1:
        print(f'Case {time} is not a tree.')
    else:
        breaking = 0
        for i in range(100):
            if visit[i] == False:
                print(f'Case {time} is not a tree.')
                breaking = 1
                break
        if breaking == 0:
            print(f'Case {time} is a tree.')