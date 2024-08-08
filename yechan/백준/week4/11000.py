# 11000
import sys
import heapq
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a.sort(key = lambda x: (x[0], x[1]))

heap = [a[0][1]]
for i in range(1,n):
    if heap[0] <= a[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, a[i][1])
    
print(len(heap))