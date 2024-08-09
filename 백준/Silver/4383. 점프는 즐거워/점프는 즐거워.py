import sys
input = sys.stdin.readline

while True:
    try:
        l = list(map(int, input().split()))
        n = [i for i in range(1, l[0])]
        for i in range(1, l[0]):
            if abs(l[i] - l[i+1]) in n:
                n.remove(abs(l[i]-l[i+1]))
        if n:
            print("Not jolly")
        else:
            print("Jolly")
    except:
        break