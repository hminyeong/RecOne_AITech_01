import sys


input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def findValue(loc):
    y, x = loc
    nums = [i+1 for i in range(9)]
    #가로
    for i in range(9):
        if sudoku[y][i] in nums:
            nums.remove(sudoku[y][i])
        if sudoku[i][x] in nums:
            nums.remove(sudoku[i][x])
    #구역
    y = y//3
    x = x//3
    for i in range(y*3, (y+1)*3):
        for j in range(x*3, (x+1)*3):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])
    return nums

def dfs(count):
    if count==len(zeros):
        for row in sudoku:
            print(*row)
        return
    
    (y, x) = zeros[count]
    values = findValue((y, x))
    for num in values:
        sudoku[y][x] = num
        dfs(count + 1)
        sudoku[y][x] = 0

dfs(0)





