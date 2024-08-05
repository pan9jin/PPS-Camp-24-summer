import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer
def bcf(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

print(bcf(n, k))