# python3 -> 시간초과
# pypy3로 제출

import sys
input = sys.stdin.readline

sudoku_num = [list(map(int, input().split())) for _ in range(9)]
zero_list = []
for i in range(9):
    for j in range(9):
        if sudoku_num[i][j] == 0:
            zero = (i, j)
            zero_list.append(zero)

def check_row(x,num): # 같은 행에 동일한 숫자가 있으면 return False, 없으면 return True
    for i in range(0,9):
        if num == sudoku_num[x][i]:
            return False
    return True

def check_col(y,num): # 같은 열에 동일한 숫자가 있으면 return False, 없으면 return True
    for i in range(0,9):
        if num == sudoku_num[i][y]:
            return False
    return True

def check_3by3(x,y,num): # 3by3 matrix에 동일한 숫자가 있으면 return False, 없으면 return True
    box_x = int(x//3)*3
    box_y = int(y//3)*3
    for i in range(3):
        for j in range(3):
            if num == sudoku_num[box_x+i][box_y+j]:
                return False
    return True

def dfs(cnt):
    if cnt == len(zero_list):
        for i in range(9):
            print(*sudoku_num[i])
        exit(0)
    for i in range(1,10): # 같은 row, col, 3by3matrix에서 1~9 숫자 확인
        x = zero_list[cnt][0] # zero 공간 x좌표
        y = zero_list[cnt][1] # zero 공간 y좌표
        if check_row(x,i) and check_col(y,i) and check_3by3(x,y,i):
            sudoku_num[x][y] = i
            dfs(cnt+1)
            sudoku_num[x][y] = 0

dfs(0)


