import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    a, b, c, d = map(int, input().split())
    l = [a, b, c]
    l.sort()
    s = sum(l) - d
    a = min(l[0], s//3)
    b = min(l[1], (s-a)//2)
    c = s - a - b
    print(a*b*c)