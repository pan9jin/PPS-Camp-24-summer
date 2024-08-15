import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
result = 0
total = 0
for i in range(n-1):
    total += x[i]
    result += x[i+1] * total
print(result)