import sys
input = sys.stdin.readline

def dfs(n, m, d):
    if d == m:
        for i in array:
            print(i, end=' ')
        print('')
        return
    for i in range(n):
        if v[i] != 1:
            v[i] = 1
            array[d] = i+1
            dfs(n, m, d+1)
            v[i] = 0        

n, m = map(int, input().split())

array = [0]*m
v = [0]*n
dfs(n, m, 0)