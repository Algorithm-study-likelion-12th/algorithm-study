#2548
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
min = 999999999
res = 0
# 아이디어 = 가장 편차가 작은 애들로 만드는 것.
data = list(map(int, input().split()))
data.sort()
for i in range(n):
    tmp = 0
    for d in data:
        tmp += abs(d - data[i])
    if tmp < min :
        min = tmp
        res = data[i]
print(res)