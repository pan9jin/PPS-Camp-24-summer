a, b = map(int, input().split())
if b > 0:
    a = a -  (a * (0.01 * b))
print(0 if a >= 100 else 1)