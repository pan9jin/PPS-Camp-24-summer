part = [0] * 5
for i in range(5):
    part[i] = sum(map(int, input().split()))
print(f"{part.index(max(part)) + 1} {max(part)}")