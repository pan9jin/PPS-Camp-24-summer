import sys
input = sys.stdin.readline

n = int(input())
l = list(input().strip())
l = list(map(int, l))
print(sum(l))