
import sys

input = sys.stdin.readline

M, N, x, y, K = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0] # 윗면 , 앞면, 오른쪽면, 왼쪽면, 뒷면, 아랫면

def move(direction):
    if direction == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif direction == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif direction == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

direction = {1 : (1, 0), 2 : (-1, 0), 3 : (0, -1), 4 : (0, 1)}
        

maps = []

for _ in range(M):
    maps.append(list(map(int, input().split())))

command = list(map(int, input().split()))

for i in command:
    if -1 < x + direction[i][0] < N and -1 < y + direction[i][1] < M:
        x += direction[i][0]
        y += direction[i][1]
        move(i)
        if maps[y][x] == 0:
            maps[y][x] = dice[5]
        
        else:
            dice[5] = maps[y][x]
            maps[y][x] = 0
        
        print(dice[0])
