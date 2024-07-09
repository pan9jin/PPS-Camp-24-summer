n = int(input())
result = []
for _ in range(n):
    l = list(map(int, input().split()))
    print(sorted(l, reverse=True)[2])