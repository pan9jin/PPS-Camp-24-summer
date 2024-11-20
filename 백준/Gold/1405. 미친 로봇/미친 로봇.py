import sys
input = sys.stdin.readline

prob = list(map(int, input().split()))
n = prob[0]
prob.remove(n)
prob = [p / 100 for p in prob]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * 29 for _ in range(29)]

result = 0
def dfs(x, y, depth, p):
    global result
    visited[x][y] = True
    for i in range(4):
        if not visited[x+dx[i]][y+dy[i]]:
            if depth >= n:
                result += p*prob[i]
            else:
                dfs(x+dx[i], y+dy[i], depth+1, p*prob[i])
    visited[x][y] = False

dfs(14, 14, 1, 1)
print(result)