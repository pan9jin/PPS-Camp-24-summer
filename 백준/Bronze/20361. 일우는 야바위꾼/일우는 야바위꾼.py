import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
sg = [0] * (n+1)
sg[x] = 1
for _ in range(k):
    a, b = map(int, input().split())
    sg[a], sg[b] = sg[b], sg[a]
print(sg.index(1))