import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        pos = q.popleft()
        if pos == k:
            return visited[k]
        for i in (pos+1, pos-1, pos * 2):
            if 0 <= i <= 10**5 and not visited[i]:
                visited[i] = visited[pos] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0] * (10**5 + 1)

print(bfs(n))