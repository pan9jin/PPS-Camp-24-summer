import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
answer = []
for num in a:
    if num < x:
        answer.append(num)
print(*answer)