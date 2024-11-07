import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))
diff_h = [h[i]-h[i-1] for i in range(1, n)]
diff_h.sort()
print(sum(diff_h[:n-k]))