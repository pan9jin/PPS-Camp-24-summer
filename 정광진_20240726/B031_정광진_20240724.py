import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
bookmark = [int(input()) for _ in range(n)]

q = deque([(a, 0)])
visited = set()
visited.add(a)

while q:
    curr, press = q.popleft()
    if curr == b:
        print(press)
        exit(0)
    if curr + 1 < 1000 and (curr + 1) not in visited:
        visited.add(curr + 1)
        q.append((curr+1, press+1))
    if curr - 1 > 0 and (curr - 1) not in visited:
        visited.add(curr - 1)
        q.append((curr-1, press+1))
    for num in bookmark:
        if num not in visited:
            visited.add(num)
            q.append((num, press+1))