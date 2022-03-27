import sys

input = sys.stdin.readline

N = int(input())

first = []
end = []

for i in range(N):
    first.append(input())

for i in range(N):
    end.append(input())

count = 0

while first:
    car = first.pop()
    
    if car != end[-1]:
        count += 1
        end.remove(car)
    else:
        end.pop()
print(count)
