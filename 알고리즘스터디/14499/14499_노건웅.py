import sys
def input(): return sys.stdin.readline().rstrip()

def change(r, c):
    if matrix[r][c] == 0:
        matrix[r][c] = dice[6]
    else:
        dice[6] = matrix[r][c]
        matrix[r][c] = 0

def moveDice(direc):
    '''
    윗 면: 1
    아랫 면: 6
    왼쩍 면: 4
    오른쪽 면: 3
    앞 면: 5
    뒷 면: 2
    동서남북 이동시 각 면에 어떤 숫자가 들어오는 지 표시하는 함수
    '''
    if direc == 1:
        dice[3], dice[1], dice[4], dice[6] = dice[1], dice[4], dice[6], dice[3]
    elif direc == 2:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    elif direc == 3:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    else:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
comm = list(map(int, input().split()))

dice = [0] * 7
move = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for c in comm:
    dr, dc = x + move[c][0], y + move[c][1]
    if 0 <= dr < n and 0 <= dc < m:
        moveDice(c)
        change(dr, dc)
        print(dice[1])
        x, y = dr, dc
