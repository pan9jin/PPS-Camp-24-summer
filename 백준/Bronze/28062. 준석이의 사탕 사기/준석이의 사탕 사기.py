import sys
input = sys.stdin.readline

n = int(input())
candy = list(map(int, input().split()))
candy.sort(reverse=True)
answer = 0
odd = []
for c in candy:
    if c % 2 == 0:
        answer += c
    else:
        odd.append(c)
if len(odd) % 2 == 0:
    answer += sum(odd)
else:
    odd.sort(reverse=True)
    odd.pop()
    answer += sum(odd)
print(answer)