import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for _ in range(k):
    a[0], b[4] = b[4], a[0]
    a.sort()
    b.sort()

print(sum(a))