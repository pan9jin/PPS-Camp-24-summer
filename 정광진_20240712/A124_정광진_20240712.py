import sys
input = sys.stdin.readline
n = int(input())
result = []
i = 2
while i <= n:
    if n%i == 0:
        result.append(i)
        n /= i
    else:
        i += 1
for num in result:
    print(num)