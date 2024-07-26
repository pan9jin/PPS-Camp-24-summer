import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

fp, ep = 0, 0
answer = float('inf')
curr_sum = a[0]

while True:
    if curr_sum < s:
        ep += 1
        if ep == n:
            break
        curr_sum += a[ep]
    else:
        curr_sum -= a[fp]
        answer = min(answer, ep - fp + 1)
        fp += 1
print(answer if answer != float('inf') else 0)