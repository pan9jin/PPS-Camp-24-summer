import sys
input = sys.stdin.readline

sec = [int(input()) for _ in range(4)]
total = sum(sec)
print(total//60)
print(total%60)