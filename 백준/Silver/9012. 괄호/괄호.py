import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    vps = input().strip()
    d = deque()
    for c in vps:
        if c == '(':
            d.append(c)
        elif c == ')':
            if d:
                d.pop()
            else:
                print('NO')
                break
    else:
        if not d:
            print('YES')
        else:
            print('NO')