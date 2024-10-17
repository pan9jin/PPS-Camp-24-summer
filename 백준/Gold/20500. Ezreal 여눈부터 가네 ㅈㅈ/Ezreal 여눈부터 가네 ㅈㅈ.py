import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(n+1) for _ in range(3)]
dp[0][1], dp[1][1], dp[2][1] = 0, 0, 1
for i in range(2, n+1):
    dp[0][i] = (dp[1][i-1]+dp[2][i-1]) % 1000000007
    dp[1][i] = (dp[0][i-1]+dp[2][i-1]) % 1000000007
    dp[2][i] = (dp[0][i-1]+dp[1][i-1]) % 1000000007
print(dp[0][n])