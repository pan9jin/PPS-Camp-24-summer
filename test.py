a, b = map(int, input().split())
l = [i for i in range(1, 1000) for _ in range(i)]
print(sum(l[i-1] for i in range(a, b+1)))