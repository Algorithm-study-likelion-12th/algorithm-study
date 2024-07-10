# 1874
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = list()
b = list()
op = list()
for _ in range(n):
    a.append(int(input()))
cnt = 0
for i in range(n):
    while (a[i] not in b):
        cnt += 1
        b.append(cnt)
        op.append("+")
    if a[i] == b[-1]:
        b.pop()
        op.append("-") 
    else:
        op = ["NO"]
        break
for o in op:
    print(o)
       