import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [0]*(k+1)
bag[0] = 0

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        bag[i] = max(bag[i], bag[i-w]+v)
print(bag[k])