import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
visited = [0] * (n+1)
Ai = list(map(int, input().split()))
s = int(input())
answer = 1

def DFS(v):
    global answer

    for i in range(2):
        if not i:
            nv = v + Ai[v]
        else:
            nv = v - Ai[v]
        if 0 <= nv < n and not visited[nv]:
            visited[nv] = 1
            answer += 1
            DFS(nv)

DFS(s - 1)
print(answer)