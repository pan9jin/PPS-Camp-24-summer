import sys
input = sys.stdin.readline

a, b = input().split()
a, b = list(a), list(b)
flag = False
for ia, i in enumerate(a):
    for ib, j in enumerate(b):
        if i == j:
            idx = [ia, ib]
            flag = True
            break
    if flag:
        break

for i in range(len(b)):
    if i == idx[1]:
        print(*a, sep='')
        continue
    for j in range(len(a)):
        if j == idx[0]:
            print(b[i], end='')
        else:
            print('.', end='')
    print()