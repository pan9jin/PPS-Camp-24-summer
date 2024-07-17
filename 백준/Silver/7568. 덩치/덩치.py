import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ranking = deque()
result = deque()

for _ in range(n):
    x, y = map(int, input().split())
    ranking.append((x, y))

for i in range(n):
    x , y = ranking[i][0], ranking[i][1]
    rank = sum(1 for a, b in ranking if a > x and b > y)
    result.append(rank+1)

for r in result:
    print(r)