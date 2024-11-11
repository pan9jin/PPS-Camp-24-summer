import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
l_sum = 0
r_sum = 0
for i in num:
    if l_sum > r_sum:
        r_sum += i
    else:
        l_sum += i

diff = l_sum - r_sum
if diff < 0:
    diff *= -1

result = 0
weight = [100, 50, 20, 10, 5, 2, 1]
if diff != 0:
    for w in weight:
        result += diff // w
        diff %= w
print(result)