import sys
input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

w_max = 0
rope = sorted(rope, reverse=True)
for i in range(n):
    w_max = max(w_max, rope[i]*(i+1))
print(w_max)