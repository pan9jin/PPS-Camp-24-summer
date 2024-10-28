import sys
input = sys.stdin.readline

t = int(input())
n_values = []
for _ in range(t):
    n_values.append(int(input()))
max_val = max(n_values)
measure = [0]*(max_val+1)
total = [0]*(max_val+1)

for i in range(1, max_val+1):
    for j in range(1, (max_val//i)+1):
        measure[i*j] += i
    total[i] = total[i-1] + measure[i]
for n in n_values:
    print(total[n])