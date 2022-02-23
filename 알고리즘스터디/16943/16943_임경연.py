import sys
from collections import defaultdict
from itertools import permutations

input = sys.stdin.readline

N, M = map(str, input().split())


N_list = [i for i in N]
N_list.sort()

comb = list(permutations(N_list, len(N)))

answers = []

for i in comb:
    if i[0] == "0":
        continue
    else:
        answers.append(int("".join(i)))

cnt = -1
for i in answers:
    if i > cnt and i < int(M):
        cnt = i
    else:
        continue

print(cnt)