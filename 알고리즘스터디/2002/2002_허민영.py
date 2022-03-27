import sys
input = sys.stdin.readline

n = int(input().strip())
car_in = dict()
car_out = []

for i in range(n):
    car_num = input().strip()
    if car_num not in car_in:
        car_in[car_num] = 0

    car_in[car_num] = i

for i in range(n):
    car_num = input().strip()

    car_out.append(car_num)
answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if car_in[car_out[i]] > car_in[car_out[j]]:
            answer += 1
            break
print(answer)