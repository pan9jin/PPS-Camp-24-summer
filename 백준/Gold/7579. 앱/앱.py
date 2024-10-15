import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)
dp = [0]*(total_cost+1)
for i in range(n):
    for c in range(total_cost, cost[i]-1, -1):
        dp[c] = max(dp[c], dp[c-cost[i]]+memory[i])

result = total_cost
for i in range(total_cost+1):
    if dp[i] >= m:
        result = min(result, i)
print(result)