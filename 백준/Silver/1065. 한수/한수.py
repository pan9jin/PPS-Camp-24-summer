import sys
input = sys.stdin.readline
n = int(input())
result = 99
if n < 100:
    print(n)
    exit(0)
for num in range(100, n+1):
    l = list(str(num))
    flag = 1
    gap = int(l[1]) - int(l[0])
    for i in range(1, len(l)):
        if int(l[i]) - int(l[i-1]) != gap:
            flag = 0
            break
    if flag:
        result+=1
print(result)