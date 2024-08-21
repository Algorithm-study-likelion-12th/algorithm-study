import sys
input = sys.stdin.readline

N = int(input())
count = [0] * N
data = [list(map(int, input().split())) for _ in range(N)]
data.reverse()

for _ in range(N - 1):
    max_value = max(data[0])
    idx = data[0].index(max_value)
    count[idx] += 1
    data[0][idx] = data[count[idx]][idx]

print(max(data[0]))
