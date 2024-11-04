import sys
import bisect
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

lis = []

for num in line:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num
print(n - len(lis))