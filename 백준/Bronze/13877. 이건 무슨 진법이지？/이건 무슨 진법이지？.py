import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, num = input().strip().split()
    e = int(num, 8) if max(list(num)) < '8' else 0
    print(int(k), e, int(num), int(num, 16))