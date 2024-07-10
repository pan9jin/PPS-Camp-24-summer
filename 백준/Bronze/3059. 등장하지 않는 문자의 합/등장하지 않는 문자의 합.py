import sys

n = int(input())
result = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    d = {chr(i):0 for i in range(ord('A'), ord('Z')+1)}
    total = 0
    for char in s:
        d[char]+=1
    for key in d.keys():
        if d[key] == 0:
            total += ord(key)
    result.append(total)
for i in range(len(result)):
    print(result[i])