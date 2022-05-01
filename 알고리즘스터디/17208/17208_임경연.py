from re import L


N, M, K = map(int, input().split())

orders = [[0, 0]]

for order in range(N):
    orders.append(list(map(int, input().split())))

dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, len(orders)):
    burger, fries = orders[i]

    for bur in range(1, M + 1):
        for fri in range(1, K + 1):
            if burger <= bur and fries <= fri:
                dp[i][bur][fri] = max(1 + dp[i - 1][bur - burger][fri - fries], dp[i - 1][bur][fri])
            else:
                dp[i][bur][fri] = dp[i - 1][bur][fri]

answer = []
for i in dp:
    tmp = list(map(max, i))
    answer.append(max(tmp))
print(max(answer))