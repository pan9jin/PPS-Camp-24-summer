import sys
input = sys.stdin.readline

n, b, h, w = map(int, input().split())
max_cost = float('inf')
for _ in range(h):
    cost = int(input())
    week = list(map(int, input().split()))
    week.sort(reverse=True)
    if week[0] < n or b < cost*n:
        continue
    max_cost = min(max_cost, cost*n)
print(max_cost if max_cost != float('inf') else "stay home")