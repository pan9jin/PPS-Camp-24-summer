import sys
input = sys.stdin.readline

code = input().strip()
n = int(input())
cnt = 0
for _ in range(n):
    a = input()
    if a.startswith(code[0:5]):
        cnt+=1
print(cnt)