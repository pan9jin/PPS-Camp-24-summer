import sys
input = sys.stdin.readline

n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]
result = 1

def count_candy():
    cnt = 1
    for i in range(n):
        c = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j-1]:
                c += 1
            else:
                c = 1
            cnt = max(cnt, c)
        c = 1
        for j in range(1, n):
            if candy[j][i] == candy[j-1][i]:
                c += 1
            else:
                c = 1
            cnt = max(cnt, c)
    return cnt

for i in range(n):
    for j in range(n):
        if i+1 < n and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            result = max(result, count_candy())
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        if j+1 < n and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            result = max(result, count_candy())
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            
print(result)