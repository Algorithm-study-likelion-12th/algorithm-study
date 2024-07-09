# 시각
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
cnt = 0

for i in range(n+1):
    for j in range(60):
        for l in range(60):
            if "3" in str(i)+str(j)+str(l):
                cnt += 1
print(cnt)


