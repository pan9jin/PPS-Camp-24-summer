import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

def bfs(x, y):
    field[x][y] = 0
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    field = [list(map(int, input().split())) for _ in range(h)]
    island = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                island += 1
                bfs(i, j)

    print(island)