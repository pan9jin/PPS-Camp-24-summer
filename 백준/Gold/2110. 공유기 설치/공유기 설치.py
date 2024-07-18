import sys
input = sys.stdin.readline
n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]

home.sort()
start, end = 1, home[-1]-home[0]
while start <= end:
    mid = (start+end) // 2
    curr = home[0]
    cnt = 1
    for i in range(1, n):
        if home[i] - mid >= curr:
            cnt += 1
            curr = home[i]
    if cnt >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)