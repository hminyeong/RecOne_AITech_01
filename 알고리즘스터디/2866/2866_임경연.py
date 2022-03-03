import sys


input = sys.stdin.readline

R, C = map(int, input().split())

a = []

for _ in range(R):
    a.append([i for i in input() if not i.startswith('\n')])

strings = []

for i in range(C):
    tmp = ''
    for j in range(R):
        tmp += a[j][i]
    
    strings.append(tmp)


cnt = 0

tmp = True
for i in range(R):
    if len(strings[0]) == 1:
        break
    
    for j in range(C):
        strings[j] = strings[j][1:]

    test = list(set(strings))

    if len(test) != C:
        break

    cnt += 1

print(cnt)

