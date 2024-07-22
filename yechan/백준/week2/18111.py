import sys
# sys.stdin = open("input.txt", "rt")

n, m, b = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

high_height = max(max(d) for d in data)
low_height = min(min(d) for d in data)

min_time = float('inf')
final_height = 0

for target_height in range(low_height, min(high_height, 256) + 1):
    time = 0
    blocks_needed = 0
    blocks_removed = 0

    for i in range(n):
        for j in range(m):
            diff = data[i][j] - target_height
            if diff > 0:
                blocks_removed += diff
                time += 2 * diff
            elif diff < 0:
                blocks_needed -= diff
                time -= diff
    if blocks_removed + b >= blocks_needed:
        if time <= min_time:
            min_time = time
            final_height = target_height

print(min_time, final_height) 
