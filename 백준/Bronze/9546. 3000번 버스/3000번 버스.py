n = int(input())
result = []
for _ in range(n):
    st = int(input())
    p = (2 ** st) - 1
    result.append(int(p))
for i in range(n):
    print(result[i])