import sys
input = sys.stdin.readline

n = int(input())
button = list(map(int, input().split()))
state = [0]*n
cnt = 0

for i in range(n):
    if state[i] != button[i]:
        state[i]^=1
        if i+1 < n:
            state[i+1]^=1
        if i+2 < n:
            state[i+2]^=1
        cnt+=1

print(cnt)