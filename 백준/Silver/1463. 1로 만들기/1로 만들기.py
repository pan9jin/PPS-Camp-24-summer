import sys
input = sys.stdin.readline
n = int(input())
seq = {1:0, 2:1}
for i in range(3, n+1):
    seq[i] = seq[i-1]+1
    if i%3 == 0:
        seq[i]=min(seq[i//3]+1, seq[i])
    if i%2 == 0:
        seq[i]=min(seq[i//2]+1, seq[i])
print(seq[n])