import sys
input = sys.stdin.readline

n = int(input())
floor, block, total = 1, 1, 1

while True:
    block += 4*floor
    total += block
    if total > n:
        break
    floor += 1

print(floor)