from itertools import combinations
def solution(prj, n, k):
    dic = {}
    total = ["zzzzzzzzzzzzzzzzzzzzzz"]
    for i in range(len(prj)):
        for j in range(len(prj[i])):
            for t in range(len(prj[i])):
                if j == t:
                    continue
                if prj[i][j] not in dic:
                    dic[prj[i][j]] = [prj[i][t]]
                else:
                    dic[prj[i][j]].append(prj[i][t])
    array = []
    for i in dic:
        array.append(i)
        dic[i] = list(set(dic[i]))
        dic[i].sort()
    array.sort()
    check = {}
    for i in array:
        check[i] = 0
    def DFS(v,check,st):
        if total[0] < st:
            return
        if v == len(array):
            if total[0] > st:
                total[0] = st
            return
        node = array[v]
        a = list(combinations(dic[node],n))
        for j in a:
            b = []
            ss = st
            cc = 0
            for l in j:
                if check[l] > k-1:
                    cc = 1
                    break
                else:
                    b.append(l)
            if cc == 0:
                for l in b:
                    check[l] += 1
                    ss += l
                DFS(v+1,check,ss)
                for l in b:
                    check[l] -= 1
    DFS(0,check,"")
    answer = total[0]
    return answer