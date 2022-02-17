import sys
from collections import defaultdict

input = sys.stdin.readline

S, E, Q = map(str, input().split())

S = int(S[0:2]) * 60 + int(S[3:5])
E = int(E[0:2]) * 60 + int(E[3:5])
Q = int(Q[0:2]) * 60 + int(Q[3:5])

answer = defaultdict(list)
cnt = 0
while True:
    try:
        t, n = map(str, input().split())
        t = int(t[0:2]) * 60 + int(t[3:5])
    except:
        break

    if t <= S:
        answer[n].append('start')
    elif t >= E and t <= Q:
        if 'start' in answer[n] and 'end' not in answer[n]:
            cnt += 1
            answer[n].append('end')


print(cnt)