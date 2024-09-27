import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([])
day = 0

for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx, my = dx[i]+x, dy[i]+y
            if 0 <= mx < n and 0<= my < m and tomato[mx][my] == 0:
                tomato[mx][my] = tomato[x][y] + 1
                q.append((mx, my))

bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day-1)