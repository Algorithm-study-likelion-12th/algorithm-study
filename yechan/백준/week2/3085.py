import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
data = [list(input()) for _ in range(n)]

#계산
def count_max():
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1,n):
            if data[i][j] == data[i][j-1]:
                count += 1
            else :
                #여기까지만 기록.
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        #열 확인
        count = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    return max_count

result = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            result = max(result, count_max())
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]

        if i+1 < n:
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            result = max(result, count_max())
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
print(result)