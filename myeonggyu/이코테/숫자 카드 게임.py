N, M = map(int, input().split())
min_value = -1

for _ in range(N):
    data = list(map(int, input().split()))
    min_data = min(data)
    min_value = max(min_data, min_value)

print(min_value)