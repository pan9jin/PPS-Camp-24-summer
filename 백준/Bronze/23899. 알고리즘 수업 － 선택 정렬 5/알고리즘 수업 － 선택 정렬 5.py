import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if a == b:
        break
    max_val = max(a[:i+1])
    if max_val != a[i]:
        a[a.index(max_val)], a[i] = a[i], a[a.index(max_val)]
print(1 if a == b else 0)    