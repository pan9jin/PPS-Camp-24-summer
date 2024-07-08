l = [int(a) for a in str(int(input()) * int(input()) * int(input()))]
num = [0] * 10
for n in l:
    num[n]+=1
for i in range(10):
    print(num[i])