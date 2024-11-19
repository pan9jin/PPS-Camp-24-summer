import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
damage = [int(input()) for _ in range(n)]
monster = [list(map(int, input().rstrip().split())) for _ in range(k)]

result = []
for i in range(n):
    dp = [[0] * 901 for _ in range(k+1)]
    time = [0]
    for hp, _ in monster:
        spend = hp // damage[i]
        if hp % damage[i] != 0:
            spend += 1
        time.append(spend)
        
    for c in range(1, k+1):
        for t in range(1, 901):
            if t >= time[c]:
                dp[c][t] = max(dp[c-1][t], monster[c-1][1] + dp[c-1][t-time[c]])
            else:
                dp[c][t] = dp[c-1][t]
                
    result.append(dp[k][-1])
result.sort(reverse=True)
print(sum(result[:m]))