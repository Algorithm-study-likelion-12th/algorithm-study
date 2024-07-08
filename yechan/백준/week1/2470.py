# 2470
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 2000000001
start = 0
end = n-1
acid, alc = 0, 0

while start < end:
    hap = data[start] + data[end]
    if abs(hap) < abs(res):
        res = abs(hap)
        acid = data[start]
        alc = data[end]
    if hap < 0:
        start += 1
    else:
        end -= 1

print(acid, alc)
    
    




