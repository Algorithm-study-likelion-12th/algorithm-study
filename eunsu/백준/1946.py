t = int(input())

for i in range(t):
    n = int(input())
    info = []
    for j in range(n):
        info.append(list(map(int, input())))
    info.sort()
    for j in range(n):
        info[i + j]
