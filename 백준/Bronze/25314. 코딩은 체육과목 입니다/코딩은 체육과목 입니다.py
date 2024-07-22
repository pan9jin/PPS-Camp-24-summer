import sys
input = sys.stdin.readline
n = int(input())
result = ''
for _ in range(n//4):
    result += 'long '
result += 'int'
print(result)