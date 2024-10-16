import sys
input = sys.stdin.readline

n = int(input())
stu = []
for _ in range(n):
    sin = list(input().split())
    name = sin[0]
    kor, math, eng = map(int, sin[1:])
    stu.append([name, kor, math, eng])
stu.sort(key=lambda x:x[0])
stu.sort(key=lambda x:x[3], reverse=True)
stu.sort(key=lambda x:x[2])
stu.sort(key=lambda x:x[1], reverse=True)
for i in range(n):
    print(stu[i][0])