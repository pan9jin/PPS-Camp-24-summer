import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
n %= 2*m
if n == 0:
    n = 2*m

hand = []
for i in range(1, m+1):
    h1, h2 = map(int, input().split())
    hand.append((h1, i))
    hand.append((h2, i))

hand.sort()
hand = deque(hand)

for _ in range(n):
    _, p = hand.popleft()
print(p)