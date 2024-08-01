import sys
input = sys.stdin.readline

while True:
    n = list(map(int, input().split()))
    if all(x == 0 for x in n):
        exit(0)
    n.sort(reverse=True)
    if n[0]**2 == (n[1]**2 + n[2]**2):
        print("right")
    else:
        print("wrong")