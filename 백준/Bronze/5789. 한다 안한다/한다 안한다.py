import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    l = list(input().rstrip())
    if l[len(l)//2] == l[len(l)//2 - 1]:
        print("Do-it")
    else:
        print("Do-it-Not")