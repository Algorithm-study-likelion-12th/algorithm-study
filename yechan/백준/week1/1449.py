# 1449
import sys
# sys.stdin = open("input.txt", "rt")
n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
res = 1
start = data[0]
for i in range(n):
    if data[i] - start > l-1 :
        res += 1
        start = data[i]
print(res)