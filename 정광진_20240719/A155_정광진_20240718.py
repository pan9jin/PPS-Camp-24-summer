import sys
input = sys.stdin.readline
k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]
start, end = 1, max(l)
prev = (start, None, end)
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for length in l:
        cnt += length // mid
    if cnt >= n:
        start = mid+1
    else:
        end = mid-1

print(end)