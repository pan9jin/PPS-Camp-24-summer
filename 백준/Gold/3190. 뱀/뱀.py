import sys
from collections import deque
input = sys.stdin.readline

n, k = int(input()), int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
d_list = [''] * 10001

for _ in range(l):
    idx, d = input().split()
    d_list[int(idx)] = d

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
direction = 1

snake = deque([(1, 1)])
result = 0
while True:
    result += 1
    x, y = snake[-1]
    nx, ny = x+dx[direction], y+dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in snake:
        snake.append((nx, ny))
        if [nx, ny] in apple:
            apple.remove([nx, ny])
        else:
            snake.popleft()
        if d_list[result] == 'L':
            direction = (direction+3)%4
        elif d_list[result] == 'D':
            direction = (direction+1)%4
    else: break
print(result)