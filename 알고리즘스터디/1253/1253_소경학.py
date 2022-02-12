n = int(input())
array = list(map(int,input().split()))
array.sort()
def search(idx):
    L = 0
    R = n-1
    while L < R:
        if L == idx:
            L += 1
        elif R == idx:
            R -= 1
        else:
            if array[L] + array[R] < array[idx]:
                L += 1
            elif array[L] + array[R] == array[idx]:
                return True
            else:
                R -= 1
    return False
cnt = 0
for i in range(n):
    if search(i):
        cnt += 1
print(cnt)
