import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

if n > m:
    boys, girls = girls, boys
    n, m = m, n

dp = [[0 for col in range(m)] for row in range(n)]
boys.sort()
girls.sort()

dp[0][0] = abs(boys[0] - girls[0])
for j in range(1, m - (n - 1)):
    dp[0][j] = min(abs(boys[0] - girls[j]), dp[0][j - 1])

for i in range(1, n):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(boys[i] - girls[j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(boys[i] - girls[j]), dp[i][j - 1])
print(dp[n - 1][m - 1])