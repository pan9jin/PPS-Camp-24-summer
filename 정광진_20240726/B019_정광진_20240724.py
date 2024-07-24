import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[0]*n for _ in range(n)]

def BFS(x, y, color, picture, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and picture[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])

def count_area(picture):
    area = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                area += 1
                BFS(i, j, picture[i][j], picture, visited)
    return area

picture = [list(input().rstrip()) for _ in range(n)]
cnt1 = count_area(picture)
for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
visited = [[0]*n for _ in range(n)]
cnt2 = count_area(picture)
print(cnt1, cnt2)