import sys
# sys.stdin = open("input.txt", "rt")

def two_pointer(n, data):
    data.sort()
    cnt = 0
    
    for k in range(n):
        i, j = 0, n-1
        while i < j:
            if i == k:
                i += 1
                continue
            if j == k:
                j -= 1
                continue
            if data[i] + data[j] == data[k]:
                cnt += 1
                break
            elif data[i] + data[j] < data[k]:
                i += 1
            else:
                j -= 1
    return cnt
            
    
n = int(input())
data = list(map(int, input().split()))
print(two_pointer(n, data))
