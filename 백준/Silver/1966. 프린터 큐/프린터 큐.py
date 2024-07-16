import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
result = []
for _ in range(t):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    l = deque()
    for i in range(n):
        l.append((i, weight[i]))
    tmp = None
    cnt = 1
    while True:
        m_val = max(l, key=lambda w: w[1])[1]
        if l[0][1] == m_val:
            if l[0][0] == m:
                break
            else:
                l.popleft()
                cnt += 1
        else:
            l.rotate(-1)
    result.append(cnt)
for r in result:
    print(r)