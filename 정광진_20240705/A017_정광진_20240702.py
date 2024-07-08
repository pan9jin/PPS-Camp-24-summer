room = [int(digit) for digit in input()]
num = {key: 0 for key in range(10)}
for n in room:
    if n == 6 or n == 9:
        if num[6] <= num[9]:
            num[6]+=1
        else:
            num[9]+=1
    else:
        num[n]+=1
print(max(num.values()))