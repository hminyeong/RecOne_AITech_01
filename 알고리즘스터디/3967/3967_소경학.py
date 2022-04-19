import sys
array = []
for _ in range(5):
    array.append(list(input()))

dic = {}
check_dic = {}
visit = [False for _ in range(12)]
for i in range(65,77):
    dic[chr(i)] = i-64
    check_dic[chr(i)] = 0
def check():
    if dic[array[0][4]] + dic[array[1][3]] + dic[array[2][2]] + dic[array[3][1]] == 26 and dic[array[0][4]] + dic[array[1][5]] + dic[array[2][6]] + dic[array[3][7]] == 26 and dic[array[1][1]] + dic[array[1][3]] + dic[array[1][5]] + dic[array[1][7]] == 26 and dic[array[3][1]] + dic[array[3][3]] + dic[array[3][5]] + dic[array[3][7]] == 26 and dic[array[1][1]] + dic[array[2][2]] + dic[array[3][3]] + dic[array[4][4]] == 26 and dic[array[1][7]] + dic[array[2][6]] + dic[array[3][5]] + dic[array[4][4]] == 26:
        return True
    return False

brray = [[0,4],[1,1],[1,3],[1,5],[1,7],[2,2],[2,6],[3,1],[3,3],[3,5],[3,7],[4,4]]
crray = []

for i in brray:
    if array[i[0]][i[1]] != 'x':
        check_dic[array[i[0]][i[1]]] = 1
    else:
        crray.append(i)
total = [0]        
def DFS(v):
    if total[0] != 0:
        return
    if v == len(crray):
        if check():
            for j in array:
                print("".join(j))
            total[0] = 1
        return
    xx, yy = crray[v][0], crray[v][1]
    for i in check_dic:
        if check_dic[i] == 0:
            array[xx][yy] = i
            check_dic[i] = 1
            DFS(v+1)
            check_dic[i] = 0          
DFS(0) 