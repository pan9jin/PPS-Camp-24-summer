n = int(input())
names = {}
for _ in range(n):
    c = input()[0]
    if c in names:
        names[c] += 1
    else:
        names[c] = 1
result = ''
for c in names:
    if names[c] >= 5:
        result+=c
result = ''.join(sorted([c for c in names if names[c] >= 5]))
print(result if result else 'PREDAJA')