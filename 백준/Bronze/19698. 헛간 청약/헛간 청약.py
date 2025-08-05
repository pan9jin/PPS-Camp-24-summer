n, w, h, l = map(int, input().split())
result = (w // l) * (h // l)
print(result if result <= n else n)