import sys
input = sys.stdin.readline

l = int(input())
s = list(input().rstrip())
result = 0
for i in range(l):
    result += (ord(s[i]) - 96) * 31**i

print(result)