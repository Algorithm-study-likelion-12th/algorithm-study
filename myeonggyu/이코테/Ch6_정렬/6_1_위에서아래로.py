N = int(input())
data = [int(input()) for _ in range(N)]

data.sort(reverse=True)

for i in data:
    print(i, end=' ')
