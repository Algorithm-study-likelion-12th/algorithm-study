# 2467
import sys
# sys.stdin = open("input.txt", "rt")

def binary_search(n, data):
    left, right = 0 , n-1
    min_sum = abs(data[left] + data[right])
    res = [data[left], data[right]]
    while left < right:
        sum = data[left] + data[right]
        if abs(sum) < min_sum :
            min_sum = abs(sum)
            res = [data[left], data[right]]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            return res
    return res
        

n = int(input())
data = sorted(list(map(int, input().split())))
a, b = binary_search(n, data)
print(a, b)