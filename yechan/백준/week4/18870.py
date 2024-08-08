import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = list(map(int, input().split()))

a = sorted(list(set(data)))
dic = {a[i] : i for i in range(len(a))}
for i in data:
    print(dic[i], end = " ")
