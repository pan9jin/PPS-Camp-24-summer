import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
dic = {}
for c in card:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1
m = int(input())
sg_card = list(map(int, input().split()))
answer = [dic[c] if c in dic.keys() else 0 for c in sg_card]
print(*answer)