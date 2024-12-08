import sys
# sys.stdin = open("input.txt", "rt")

def count(data, k):
    return sum(d // k for d in data)

def binary_search(data, n):
    start, end = 1, max(data)
    while start <= end:
        mid = start + (end - start) // 2
        if count(data, mid) >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end  

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
print(binary_search(data, n))