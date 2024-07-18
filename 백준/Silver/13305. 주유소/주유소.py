import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
tot_price = 0
price = oil[0]
for i in range(n-1):
    if price > oil[i]:
        price = oil[i]
    tot_price += price * road[i]
print(tot_price)