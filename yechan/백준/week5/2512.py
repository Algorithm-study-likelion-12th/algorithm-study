# 2512
import sys
# sys.stdin = open("input.txt", "rt")

def count(data, target):
    res = 0
    for d in data:
        if target >= d:
            res += d
        else:
            res += target
    return res

def binary_search(data):
    start, end = 1, max(data)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if count(data, mid) <= money:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result 

n = int(input())
data = sorted(list(map(int, input().split())))
money = int(input())
print(binary_search(data))