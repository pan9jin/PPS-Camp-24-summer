import sys
input = sys.stdin.readline
n = int(input())
def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a
result = []
for _ in range(n):
    a, b = map(int, input().split())
    result.append((a*b) // gcd(a, b))
for num in result:
    print(num)