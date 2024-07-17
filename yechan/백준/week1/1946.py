# 1946
import sys
# sys.stdin = open("input.txt", "rt")
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    test = []
    cnt = 0
    #document = a, interview = b
    for j in range(n):
        a, b = map(int, sys.stdin.readline().split())
        test.append([a,b])
    test.sort()
    min_rank = float('inf')
    for i in range(n):
        if test[i][1] < min_rank:
            cnt += 1
            min_rank = test[i][1]
            continue  
    print(cnt)

