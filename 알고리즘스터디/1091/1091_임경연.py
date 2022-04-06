import sys
import copy

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))
S = list(map(int, input().split()))

ideal = [0, 1, 2] * (int(N / 3))

state = copy.deepcopy(P)

answer = 0

while True:
    if state == ideal:
        print(answer)
        break
    elif state == P and answer != 0:
        print(-1)
        break
    
    t = [-1 for _ in range(N)]

    for i, move in enumerate(S):
        t[move] = state[i]
    
    state = copy.deepcopy(t)

    answer += 1


