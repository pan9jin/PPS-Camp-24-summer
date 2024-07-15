import sys, math
input = sys.stdin.readline
t = int(input())
result = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d == 0 and r1 == r2:
        result.append(-1)
    elif d == (r1+r2) or d == abs(r1 - r2):
        result.append(1)
    elif abs(r1 - r2) < d < (r1+r2):
        result.append(2)
    else:
        result.append(0)
for r in result:
    print(r)