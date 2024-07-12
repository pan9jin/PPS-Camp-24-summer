n = 1000 - int(input())
cnt = 0
charge = [500, 100, 50, 10, 5, 1]
for c in charge:
    i = n//c
    cnt += i
    if i != 0:
        n -= (i*c)
print(cnt)