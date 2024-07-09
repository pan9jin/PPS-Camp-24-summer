n = int(input())
l = []
for i in range(n):
    age, name = input().split()
    l.append((int(age), name, i))
l = sorted(l, key=lambda x:(x[0], x[2]))
for age, name, _ in l:
    print(age, name)