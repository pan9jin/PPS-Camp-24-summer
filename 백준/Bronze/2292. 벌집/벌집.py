import sys
input = sys.stdin.readline

n = int(input())
box = 1
cnt = 1
while n > box:
    box += 6*cnt
    cnt += 1
print(cnt)