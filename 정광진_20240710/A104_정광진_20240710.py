from collections import deque
n = int(input())
l = deque((map(int, input().split())))
result = []
tot_sum = sum(l)
for _ in range(n):
    result.append(tot_sum - l[-1])
    l.rotate(1)
print(min(result))