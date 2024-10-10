import sys
input = sys.stdin.readline

while 1:    
    n, m = map(float, input().split())
    if n == 0 and m == 0:
        break
    n, m = int(n), int(m*100+0.5)
    candy = []
    dp = [0]*(m+1)
    for _ in range(n):
        cal, price = map(float, input().split())
        cal, price = int(cal), int(price*100+0.5)
        
        for i in range(price, m+1):
            dp[i] = max(dp[i], dp[i-price]+cal)
            
    print(dp[m])