n = int(input())
time = list(map(int, input().split()))
y = sum((t//30 + 1) * 10 for t in time)
m = sum((t//60 + 1) * 15 for t in time)
if y < m:
    print(f"Y {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y M {y}")