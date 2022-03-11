n, m = map(int, input().split())
k = int(input())
cons = set()
d = [[0] * (n + 1) for _ in range(m + 1)]
d[0][0] = 1 # 출발점

for i in range(k): # 공사중에 ㄴ도로의 양 끝점을 출발점에서 가까운 순서대로
    a1, b1, a2, b2 = map(int, input().split())
    if (a1 > a2):
        a1, a2 = a2, a1
    if (b1 > b2):
        b1, b2 = b2, b1
    cons.add(((a1, b1), (a2, b2)))

for i in range(1, m + 1):
    if (((0, i - 1), (0, i)) in cons):
        continue
    d[i][0] = d[i - 1][0]

for i in range(1, n + 1):
    if (((i - 1, 0), (i, 0)) in cons):
        continue
    d[0][i] = d[0][i - 1]

for x in range(1, n + 1):
    for y in range(1, m + 1):
        if (((x - 1, y), (x, y)) in cons and ((x, y - 1), (x, y)) in cons):
            continue
        
        if (((x - 1, y), (x, y)) in cons):
            d[y][x] = d[y - 1][x]
        elif (((x, y - 1), (x, y)) in cons):
            d[y][x] = d[y][x - 1]
        else:
            d[y][x] = d[y][x - 1] + d[y - 1][x]

print(d[m][n]) # y좌표이기 때문에 [m][n]으로 출력
