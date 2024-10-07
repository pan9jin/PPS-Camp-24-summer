import sys
input = sys.stdin.readline

d, k = map(int, input().split())
dp = []
dp.append(0)
dp.append(1)
for i in range(2, d):
    dp.append(dp[i-1]+dp[i-2])

a, b= dp[d-2], dp[d-1]
for i in range(1, k):
    if (k-i*a)%b == 0:
        print(i)
        print((k-i*a)//b)
        break