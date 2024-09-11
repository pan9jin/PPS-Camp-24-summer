import sys
input = sys.stdin.readline

d, p = map(int, input().split())

dp = [-1] * (d+1)
dp[0] = float('inf')

for _ in range(p):
    l, c = map(int, input().split())
    for i in range(d, l-1, -1):
        dp[i] = max(dp[i], min(dp[i-l], c))

print(dp[d])