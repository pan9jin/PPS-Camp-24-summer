import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
k = 1
for i in range(1, n):
    if (a[i-1]+a[i])%2 == 1:
        k += 1
print(k)