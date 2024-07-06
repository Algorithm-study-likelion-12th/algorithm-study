# 1931
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
data = []
for _ in range(n):
    time = list(map(int, input().split()))
    data.append(time)
data.sort(key = lambda x:(x[1], x[0]))

start = 0
end = 0
res = 0
for d in data:
    if d[0] >= end:
        res += 1
        end = d[1]
print(res)
