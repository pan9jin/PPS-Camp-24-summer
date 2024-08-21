import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    c = list(input().rstrip().split())
    if len(c) == 1:
        if c[0] == 'all':
            s = {i for i in range(1, 21)}
        elif c[0] == 'empty':
            s = set()
    else:
        comm, v = c[0], int(c[1])
        if comm == 'add':
            s.add(v)
        elif comm == 'remove':
            s.discard(v)
        elif comm == 'check':
            print(1 if v in s else 0)
        elif comm == 'toggle':
            if v in s:
                s.discard(v)
            else:
                s.add(v)