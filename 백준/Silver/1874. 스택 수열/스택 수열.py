import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
max_v = 1
stack, answer, find = deque(), deque(), True
for _ in range(n):
    num = int(input())
    while max_v <= num:
        stack.append(max_v)
        answer.append('+')
        max_v += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        find = False
if not find:
    print('NO')
else:
    for c in answer:
        print(c)