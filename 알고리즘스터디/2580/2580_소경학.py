import sys

def promise(i,j,k):
    
    for m in range(9):
        if k in sudoku[i]:
            return False
        elif sudoku[m][j] == k:
            return False
    
    for l in range(3):
        for o in range(3):
            if sudoku[i//3*3+l][j//3*3+o] == k:
                return False
    return True

def solve(cnt):
    if cnt == n:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print()
        sys.exit(0)
    else:
        for k in range(1,10):
            i = zero[cnt][0]
            j = zero[cnt][1]
            if promise(i,j,k):
                sudoku[i][j] = k
                solve(cnt+1)
                sudoku[i][j] = 0

n = 0
flag = 0
sudoku = []
zero = []
for _ in range(9):
    sudoku.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append([i,j])
n=len(zero)
solve(0)