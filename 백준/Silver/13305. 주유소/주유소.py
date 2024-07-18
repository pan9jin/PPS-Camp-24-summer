import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
oil = oil[:-1]
price = 0
for i in range(n-1):
    m_price = min(oil)
    if oil[i] == m_price:
        price += oil[i] * sum(road[i:n])
        break
    elif oil[i] > oil[i+1]:
        price += oil[i] * road[i]
print(price)