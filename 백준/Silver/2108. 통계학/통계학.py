import sys
input = sys.stdin.readline
n = int(input())
l = []
freq = {}
for _ in range(n):
    num = int(input())
    l.append(num)
    if num not in freq:
        freq[num] = 1
    else:
        freq[num]+=1
cnt = len(l)
mean = int(round(sum(l)/cnt))
median = (sorted(l)[cnt//2] + sorted(l)[cnt//2-1])/2 if cnt%2 == 0 else sorted(l)[cnt//2]
max_num = max(freq.values())
check = 0
mode = 0
for i in sorted(set(l)):
    if freq[i] == max_num:
        mode = i
        check += 1
    if check == 2:
        break
print(mean)
print(median)
print(mode)
print(max(l) - min(l))