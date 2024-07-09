n = int(input())
s = sorted(set(list(map(int, input().split()))))
print(*s)