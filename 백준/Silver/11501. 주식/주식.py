import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    purchase = price[-1]
    profit = 0
    for i in range(n-2, -1, -1):
        purchase = max(purchase, price[i])
        if purchase > price[i]:
            profit += purchase-price[i]
    print(profit)