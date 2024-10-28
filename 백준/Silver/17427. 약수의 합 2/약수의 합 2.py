import sys
input = sys.stdin.readline

n = int(input())
result = sum(k*(n//k) for k in range(1, n+1))
print(result)