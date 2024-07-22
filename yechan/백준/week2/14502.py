import sys
# sys.stdin = open("input.txt", "rt")
import itertools
from collections import deque
import copy

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
w = 3 #wall

empty_cells = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 0]
virus_cells = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 2]
wall_combinations = list(itertools.combinations(empty_cells, w))

def spread_virus(data, virus_cells):
    directions = [(-1,0), (1,0), (0, -1), (0,1)]
    queue = deque(virus_cells)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                data[nx][ny] = 2
                queue.append((nx, ny))

def count_safe_area(data):
    return sum(row.count(0) for row in data)

max_safe_area = 0

for walls in wall_combinations:
    temp_data = copy.deepcopy(data)
    for wx, wy in walls:
        temp_data[wx][wy] = 1
    spread_virus(temp_data, virus_cells)
    safe_area = count_safe_area(temp_data)
    max_safe_area = max(safe_area, max_safe_area)

print(max_safe_area)
