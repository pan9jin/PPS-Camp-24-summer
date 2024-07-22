import sys
input = sys.stdin.readline
n = int(input())
print(sum(num+1 for num in range(n)))