import sys
input = sys.stdin.readline

n = int(input())
l1 = set(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

for i in l2:
    if i in l1:
        print('1')
    else:
        print('0')