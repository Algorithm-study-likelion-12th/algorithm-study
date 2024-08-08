import sys
#sys.stdin = open("input.txt", "rt", encoding="utf-8")

import heapq

def nth(n, table):
    min_heap = []
    
    for row in table:
        for num in row:
            if len(min_heap) < n:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heapreplace(min_heap, num)
    
    return min_heap[0]
            
n = int(input().strip())
table = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    table.append(row)

nth_largest = nth(n, table)
print(nth_largest)


