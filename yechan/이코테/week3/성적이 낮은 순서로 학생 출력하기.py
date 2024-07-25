import sys
sys.stdin = open("input.txt", "rt", encoding="utf-8")

n = int(input())
data = []
for _ in range(n):
    line = input().split()
    data.append((line[0], int(line[1])))

data.sort(key = lambda x:x[1])

for i in data:
    print(i[0])