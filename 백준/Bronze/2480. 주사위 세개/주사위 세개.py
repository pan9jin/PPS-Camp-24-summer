import sys
input = sys.stdin.readline
l = list(map(int, input().split()))
dice = {}
result = 0
for num in l:
    if num not in dice:
        dice[num] = 1
    else:
        dice[num] += 1
max_val = max(dice.values())
max_idx = [k for k, v in dice.items() if v == max_val]
if max_val == 3:
    result = 10000 + (1000 * max_idx[0])
elif max_val == 2:
    result = 1000 + (100 * max_idx[0])
else:
    result = 100 * max(max_idx)
print(result)