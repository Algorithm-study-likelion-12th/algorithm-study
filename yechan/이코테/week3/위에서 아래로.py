import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
for i in data:
    print(i, end = ' ')

