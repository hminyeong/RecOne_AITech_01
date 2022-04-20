import sys
input = sys.stdin.readline

str_1 = sys.stdin.readline().strip()
str_2 = sys.stdin.readline().strip()

dp = [[0] * len(str_2) for _ in range(len(str_1))]
result = 0

for i in range(len(str_1)):
    for j in range(len(str_2)):
        if str_1[i] == str_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])

print(result)