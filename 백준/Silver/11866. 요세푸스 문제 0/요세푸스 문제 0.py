from collections import deque
nk = list(map(int, input().split()))
l = deque([i+1 for i in range(nk[0])])
result = deque()
while len(l) > 0:
    l.rotate(-(nk[1]-1))
    result.append(str(l.popleft()))

result = '<' + ', '.join(result) + '>'
print(result)