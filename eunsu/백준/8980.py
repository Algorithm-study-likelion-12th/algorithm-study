n, limit = map(int, input().split())
m = int(input())
deliveries = [list(map(int, input().split())) for i in range(m)]
space = [limit for i in range(n + 1)]
deliveries.sort(key=lambda x: x[1])
result = 0

for i in deliveries:
    min_box = limit
    for j in range(i[0], i[1]):
        min_box = min(min_box, space[j])
    min_box = min(min_box, i[2])
    for j in range(i[0], i[1]):
        space[j] -= min_box
    result += min_box

print(result)
