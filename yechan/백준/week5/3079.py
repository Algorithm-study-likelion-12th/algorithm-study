# 3079
import sys
# sys.stdin = open("input.txt", "rt")


def binary_search(data, m):
    #최소 크기
    start = 1
    #최대 크기
    end = m * max(data)
    while start < end:
        res = (start + end) // 2
        count = 0
        for d in data:
            count += res // d
        if count >= m:
            end = res
        else:
            start = res + 1
    return start
            
            
n, m = map(int, input().split())
data = sorted([int(input()) for _ in range(n)])
print(binary_search(data, m))