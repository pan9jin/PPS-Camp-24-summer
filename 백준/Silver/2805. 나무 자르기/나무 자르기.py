import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
prev = (start, None, end)
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for length in tree:
        if length > mid:
            cnt += length - mid
    if cnt >= m:
        start = mid+1
    else:
        end = mid-1

print(end)