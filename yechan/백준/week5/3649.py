# 3649
import sys
sys.stdin = open("input.txt", "rt")
# 0이 7개여야함.

def binary_search(data, m):
    start, end = 0, m-1
    while start < end:
        if data[start] + data[end] == n * 1e7:
            return data[start], data[end]
        elif data[start] + data[end] < n * 1e7:
            start += 1
        else:
            end -= 1
    return 0, 0
            

while True: 
    try:           
        n = int(input())
        m = int(input())
        data = sorted([int(input()) for _ in range(m)])
        a, b = binary_search(data, m)
        if (a, b) == (0, 0):
            print("danger")
        else:
            print("yes", a, b)
    except EOFError:
        break
    