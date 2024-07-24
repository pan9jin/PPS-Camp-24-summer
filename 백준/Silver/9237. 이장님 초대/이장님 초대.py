import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)
answer = 0
for i in range(len(t)):
    answer = max(answer, t[i] + i + 1)

print(answer+1)