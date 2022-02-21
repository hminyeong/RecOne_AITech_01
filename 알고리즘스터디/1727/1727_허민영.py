import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_style = sorted(list(map(int, input().split())))
m_style = sorted(list(map(int, input().split())))

if n > m: 
    n_style, m_style = m_style, n_style
    n, m = m, n
    
dp = [[0] * m for __ in range(n)]

dp[0][0] = abs(n_style[0] - m_style[0])

for j in range(1, m - (n - 1)):
    dp[0][j] = min(abs(n_style[0] - m_style[j]), dp[0][j - 1])
    
for i in range(1, n):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(n_style[i] - m_style[j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(n_style[i] - m_style[j]), dp[i][j - 1])
            
print(dp[n - 1][m - 1])
