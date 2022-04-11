import sys
from math import gcd

input = sys.stdin.readline

X, Y = map(int, input().split())

x, y, dx, dy = map(int, input().split())

def distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def minSlope(dx, dy):
    a = gcd(abs(dx), abs(dy))

    return dx/a, dy/a

dx, dy = minSlope(dx, dy)

answer = [0, 0]
min_dist = int(1e100)

while True:
    dist = distance(X, Y, x, y)
    if dist < min_dist:
        min_dist = dist
        answer = [int(x), int(y)]
        x += dx
        y += dy
    else:
        print(*answer)
        break
    


