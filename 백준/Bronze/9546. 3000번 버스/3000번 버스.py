n = int(input())
result = []
for _ in range(n):
    st = int(input())
    p = 0
    for _ in range(st):
        p += 0.5
        p *= 2
    result.append(int(p))
for i in range(n):
    print(result[i])