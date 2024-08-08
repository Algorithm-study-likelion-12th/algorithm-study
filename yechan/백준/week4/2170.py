# 2170
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = sorted([list(map(int, input().split())) for i in range(n)])
res = a[0][1] - a[0][0]
cur_start, cur_end = a[0][0], a[0][1]

for i in range(n-1):
    post_start, post_end = a[i+1][0], a[i+1][1]
    if cur_end >= post_end:
        continue
    elif cur_end >= post_start:
        res += post_end - cur_end
        cur_end = post_end
    elif post_start > cur_end:
        res += post_end - post_start
        cur_end = post_end
print(res)
        
    
    




