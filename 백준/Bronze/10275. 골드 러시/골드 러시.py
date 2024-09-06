import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    day = 0
    t = bin(min(a, b))[::-1].index('1')
    print(n-t)