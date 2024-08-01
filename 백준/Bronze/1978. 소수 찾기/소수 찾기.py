import sys
import math
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
cnt = 0
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

for i in num:
    if is_prime(i):
        cnt+=1
print(cnt)