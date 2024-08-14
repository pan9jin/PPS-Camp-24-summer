import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
f = list(map(int, input().rstrip().split()))
if sum(f) >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")