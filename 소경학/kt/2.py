import sys
sys.setrecursionlimit(10**6)
def solution(n, info):
    array = [[] for _ in range(100)]
    for i in info:
        array[i[0]].append([i[1],i[2]])
        array[i[1]].append([i[0],-i[2]])
    total = [999999999999]
    visit = [False for _ in range(100)]
    visit[1] = True
    def DFS(node,num):
        if num > total[0]:
            return
        if node == n:
            total[0] = min(num,total[0])
            return
        for i in array[node]:
            if visit[i[0]] == False:
                if num == 0:
                    if i[1] < 0:
                        visit[i[0]] = True
                        DFS(i[0],-i[1]*2)
                        visit[i[0]] = False
                    else:
                        visit[i[0]] = True
                        DFS(i[0],num+i[1])
                        visit[i[0]] = False
                else:
                    if i[1] < 0: 
                        if -i[1] >= num: # 1 -4 2 -4 3 -4
                            visit[i[0]] = True
                            DFS(i[0],-i[1]*2)
                            visit[i[0]] = False
                        else:
                            # 5 -4 8 -4 11 -4 12 -4 13 -4
                            if num//(-i[1]) % 2 == 0: # ¸òÀÌ Â¦
                                check = num // (-i[1]) + 1
                            else: # ¸òÀÌ È¦
                                if num % (-i[1]) == 0:
                                    check = num // (-i[1])
                                else:
                                    check = num // (-i[1]) + 2
                            visit[i[0]] = True
                            DFS(i[0],-i[1]*check+(-i[1]))
                            visit[i[0]] = False
                    elif i[1] > 0:
                        if 2*i[1] >= num:
                            visit[i[0]] = True
                            DFS(i[0],3*i[1])
                            visit[i[0]] = False
                        else: 
                            if (num // i[1]) % 2 == 0:
                                if num % i[1] == 0:
                                    visit[i[0]] = True
                                    DFS(i[0],num + i[1])
                                    visit[i[0]] = False
                                else:
                                    check = num // i[1] + 2
                                    visit[i[0]] = True
                                    DFS(i[0],i[1]*check + i[1])
                                    visit[i[0]] = False
                            else: # 12 13 14 15
                                if num % i[1] == 0:
                                    visit[i[0]] = True
                                    DFS(i[0],num + 2*i[1])
                                    visit[i[0]] = False
                                else:
                                    visit[i[0]] = True
                                    check = num // i[1] + 1
                                    DFS(i[0],i[1]*check + i[1])
                                    visit[i[0]] = False
    DFS(1,0)
    if total[0] == 999999999999:
        total[0] = -1  
    answer = total[0]
    return answer