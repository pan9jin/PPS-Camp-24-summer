import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

bst = []
while True:
    try:
        bst.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if bst[i] > bst[start]:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(bst[start])

postorder(0, len(bst) - 1)