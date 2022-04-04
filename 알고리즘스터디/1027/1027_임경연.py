import sys

input = sys.stdin.readline

N = int(input())

H = list(map(int, input().split()))

def slope(b1, b2):
    x1, y1 = b1
    x2, y2 = b2

    # 기울기
    a = (y2 - y1) / (x2 - x1)

    # y절편
    b = y2 - a * x2

    return (a, b)

answer = 0

for i in range(N):
    token = N-1

    for j in range(N):
        if i == j:
            continue
        else:
            if i < j:
                a, b = slope((i, H[i]), (j, H[j]))

                for k in range(i + 1, j):
                    if H[k] >= a * k + b:
                        token -= 1
                        break
            
            else:
                a, b = slope((i, H[i]), (j, H[j]))

                for k in range(j + 1, i):
                    if H[k] >= a * k + b:
                        token -= 1
                        break
    
    answer = max(answer, token)

print(answer)