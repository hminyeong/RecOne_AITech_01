import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    check = False
    array = []
    for _ in range(n):
        array.append(sys.stdin.readline().rstrip())
    array.sort()
    for i in range(n-1):
        if array[i] == array[i+1][:len(array[i])]:
            check = True
    if check:
        print('NO')
    else:
        print('YES')