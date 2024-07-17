import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
max_curr = max_global = l[0]

for i in range(1, len(l)):
    max_curr = max(l[i], max_curr + l[i])
    if max_curr > max_global:
        max_global = max_curr
print(max_global)