import sys
input = sys.stdin.readline
n = int(input())
time = list(map(int, input().split()))
time = sorted(time)
dp = [0]*n
dp[0] = time[0]
for i in range(1, n):
    dp[i] = time[i] + dp[i-1]
print(sum(dp))