import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
l.sort(key = lambda v:(v[1], v[0]))

for [x, y] in l:
    print(x, y)