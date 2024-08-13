import sys
input = sys.stdin.readline

n = int(input())
d = {}
l = []
for _ in range(n):
    num = int(input())
    if not num in d:
        d[num] = 1
        l.append(num)
    else:
        d[num]+=1
l.sort()
for num in l:
    for _ in range(d[num]):
        print(num)