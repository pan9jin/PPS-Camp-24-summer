import sys
input = sys.stdin.readline

n, k = map(int, input().split())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)
cnt = 0

for p in price:
    if k == 0:
        break
    cnt += k // p
    k %= p

print(cnt)