import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    a, b, c, d = map(int, input().split())
    l = [a, b, c]
    for _ in range(d):
        l.sort()
        l[-1] -= 1
    print(l[0] * l[1] * l[2])