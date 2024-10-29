import sys
input = sys.stdin.readline

prime = [i for i in range(1000001)]
prime[1] = 0

for i in range(2, int(len(prime)**0.5)+1):
    if prime[i] == 0:
        continue
    for j in range(i*2, len(prime), i):
        prime[j] = 0

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, n//2 + 1, 2):
        if prime[i] and prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
