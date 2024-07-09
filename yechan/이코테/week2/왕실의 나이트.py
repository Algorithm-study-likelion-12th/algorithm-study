# 왕실의 나이트
import sys
# sys.stdin = open("input.txt", "rt")

dx = [-2,-2,-1,1,2,2,-1,1]
dy = [-1,1,2,2,-1,1,-2,-2]
cnt = 0

a = list(input())
x = ord(a[0])-96
y = int(a[1])
for i in range(8):
    x = x + dx[i]
    y = y + dy[i]
    if x < 1 or x > 8 or y < 1 or y > 8:
        continue
    else:
        cnt += 1
print(cnt)
