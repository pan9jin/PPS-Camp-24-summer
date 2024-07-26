import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INT_MAX = float('inf')

n = int(input())
s = list(input())

dp = [[0] * 2 for _ in range(n)]
if s[0] == 'A':
    dp[0][0] = 0
    dp[0][1] = 1
else:
    dp[0][0] = 1
    dp[0][1] = 0

for i in range(1, n):
    if s[i] == 'A':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] + 1
    else:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1]

    dp[i][0] = min(dp[i][0], dp[i - 1][1] + 1)
    dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)

print(dp[n - 1][0])