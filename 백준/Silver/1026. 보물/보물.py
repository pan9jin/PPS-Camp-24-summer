n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = sum(a * b for a, b in zip(sorted(a), sorted(b, reverse=True)))
print(f"{s}")