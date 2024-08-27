import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
s = set()
for _ in range(n):
    l = input().rstrip().split()
    streak, name = l[:m], l[m]

    cnt = 0
    day = 0
    for c in streak:
        if c == '.':
            cnt += 1
        else:
            cnt = 0
        day = max(day, cnt)
    rs.append([day, name])
    s.add(day)

print(len(s))
for k in rs:
    print(*k)