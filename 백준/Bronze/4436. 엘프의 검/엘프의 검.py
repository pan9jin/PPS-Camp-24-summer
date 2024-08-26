import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    
    test = {f'{i}':False for i in range(0, 10)}
    
    cnt = 0
    s = k = 0
    while cnt < 10:
        k += 1
        s += n
        for c in str(s):
            if not test[c]:
                test[c] = True
                cnt += 1
                if cnt == 10:
                    break
    print(k)