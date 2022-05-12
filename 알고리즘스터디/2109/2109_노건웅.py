import sys
def input(): return sys.stdin.readline().rstrip()

# 해당 일자에서 얻을 수 있는 최댓값을 고른다.

n = int(input())
lecture = [tuple(map(int,input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (-x[0],-x[1]))
day = [0] * 10001

for p, d in lecture:
    for j in range(d,0,-1):
        if day[j] == 0:
            day[j] = p
            break

print(sum(day))
