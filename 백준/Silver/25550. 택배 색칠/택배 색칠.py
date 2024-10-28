import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        min_box = max(0, box[i][j] - 1)
        for k in range(4):
            if 0 <= i+dy[k] < n and 0 <= j+dx[k] < m:
                min_box = min(min_box, box[i+dy[k]][j+dx[k]])
            else:
                min_box = 0
        result += min_box
print(result)