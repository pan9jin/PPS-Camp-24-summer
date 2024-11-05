import sys
input = sys.stdin.readline

def get_distance(a, b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5

def dfs(start, visited):
    if visited == (1 << n) - 1:
        return distance[start][0]
    
    if dp[start][visited] != float('inf'):
        return dp[start][visited]
    
    for i in range(1, n):
        if visited & (1 << i) or distance[start][i] <= 0: continue
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + distance[start][i])

    return dp[start][visited]

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * n for _ in range(n)]
dp = [[float('inf')] * (1 << n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: continue
        distance[i][j] = get_distance(city[i], city[j])

print(dfs(0, 1))