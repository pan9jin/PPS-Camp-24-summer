import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
result = 0
v = int(input())
for num in l:
    if num == v:
        result += 1
print(result)