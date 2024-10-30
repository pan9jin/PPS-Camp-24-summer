import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]
height.sort()

tot_h = sum(height)
for i in range(len(height)):
    if len(height) == 7:
        break
    for j in range(i+1, len(height)):
        if tot_h - height[i] - height[j] == 100:
            height.remove(height[j])
            height.remove(height[i])
            break

for h in height:
    print(h)