import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

board = [list(input().split()) for _ in range(5)]
def DFS(x, y, num):
    if len(num) == 6:
        unique.add(int(''.join(num)))
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            DFS(nx, ny, num + board[nx][ny])

cnt = 0
unique = set()
for i in range(5):
    for j in range(5):
        DFS(i, j, board[i][j])

print(len(unique))