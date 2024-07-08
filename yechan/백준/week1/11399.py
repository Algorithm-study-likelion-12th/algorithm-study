#11399
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
res = 0
data = list(map(int, input().split()))
data.sort(reverse=True)
for i in range(n):
    res += data[i] * (i+1)
print(res)