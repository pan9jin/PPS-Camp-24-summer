import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n*2):
    print('@'*n, end='')
    print(' '*n*3, end='')
    print('@'*n)
for _ in range(n):
    print('@'*n*5)
for _ in range(n):
    print('@'*n, end='')
    print(' '*n*3, end='')
    print('@'*n)
for _ in range(n):
    print('@'*n*5)