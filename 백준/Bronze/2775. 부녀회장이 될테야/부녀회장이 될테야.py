t = int(input())
l = [0] * t
for case in range(t):
    k = int(input())
    n = int(input())
    
    apart = [[0] * (n+1) for _ in range(k+1)]
    for i in range(n+1):
        apart[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]
    l[case] = apart[k][n]

for i in range(t):
    print(l[i])