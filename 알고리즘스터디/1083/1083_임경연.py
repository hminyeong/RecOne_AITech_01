import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

token = int(input())
cnt = 0
limit = len(numbers)

while token != 0:
    if cnt == limit:
        break
    a = numbers.index(max(numbers[cnt:limit]))
    a_ = max(numbers[cnt:limit])
    if a - cnt <= token and a - cnt != 0:
        token = token - (a - cnt)
        del numbers[a]
        numbers.insert(cnt, a_)
        cnt += 1
        limit = len(numbers)
    else:
        if a - cnt == 0:
            cnt += 1
            continue
        else:
            limit = a
        

        

numbers = [str(i) for i in numbers]

print(" ".join(numbers))