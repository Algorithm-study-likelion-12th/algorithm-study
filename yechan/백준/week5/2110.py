# 2110
import sys
#sys.stdin = open("input.txt", "rt")

def can_install(houses, distance, c):
    count = 1
    last = houses[0]
    for house in houses:
        if house - last >= distance:
            count += 1
            last = house
        if count >= c:
            return True
    return False

def binary_search(houses, c):
    start, end = 1, houses[-1] - houses[0]
    result = 0
    
    while start <= end:
        mid = (start + end)//2
        if can_install(houses, mid, c) == True:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result 

n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])
print(binary_search(houses, c))