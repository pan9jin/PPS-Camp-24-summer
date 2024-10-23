import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    stu, apple = map(int, input().split())
    result += (apple % stu)
print(result)