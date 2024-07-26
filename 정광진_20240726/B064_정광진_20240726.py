import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()

fp, ep = 0, len(a)-1
cnt = 0
while fp != ep:
    if a[fp] + a[ep] == x:
        ep -= 1
        cnt+=1
    else:
        if a[fp] + a[ep] < x:
            fp += 1
        else:
            ep -= 1
print(cnt)