# 2343
import sys
sys.stdin = open("input.txt", "rt")

def count(data, k):
    cnt = 1
    capacity = 0
    for d in data:
        if capacity + d > k:
            cnt += 1
            capacity = d
        else:
            capacity += d
    return cnt

def binary_search(data, m):
    #최소 크기
    start = max(data)
    #최대 크기
    end = sum(data)
    while start < end:
        res = (start + end) // 2
        if count(data, res) > m:
            start = res + 1
        else:
            end = res 
    return start
            
            
n, m = map(int, input().split())
data = list(map(int, input().split()))
print(binary_search(data, m))