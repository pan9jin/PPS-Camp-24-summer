import sys
input = sys.stdin.readline

n = int(input())

def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n <= 0:
    print(0)
else:
    rate = [int(input()) for _ in range(n)]
    r_num = custom_round(n*0.15)
    rate.sort()
    if r_num > 0:
        print(custom_round(sum(rate[r_num:-r_num]) / len(rate[r_num:-r_num])))
    else:
        print(custom_round(sum(rate)/len(rate)))