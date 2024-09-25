import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    x = deque(eval(input().rstrip()))
    isError = False
    r = 1
    for c in p:
        if c == 'R':
            r*=-1
        else:
            if len(x) == 0:
                isError = True
                break
            if r == 1:
                x.popleft()
            else:
                x.pop()
    if isError:
        print('error')
    else:
        if r == 1:    
            print(f"[{','.join(map(str, x))}]")
        else:
            x.reverse()
            print(f"[{','.join(map(str, x))}]")