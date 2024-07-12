import sys
input = sys.stdin.readline
n = int(input())
result = 0
for num in range(1, n+1):
    if num < 100:
        result += 1
    else:
        l = [int(a) for a in str(num)]
        if l[2]-l[1] == l[1]-l[0]:
            result+=1
print(result)