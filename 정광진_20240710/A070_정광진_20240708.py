from collections import deque

n = int(input())
l = deque([i+1 for i in range(n)])
while len(l) > 1:
    l.popleft()
    l.rotate(-1)
print(l[0])