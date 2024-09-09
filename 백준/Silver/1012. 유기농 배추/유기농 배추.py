import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    field[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    bug = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                bug += 1
                bfs(i, j)
    print(bug)