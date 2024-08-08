import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
res = 0
max_count = 0

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 2  # 방문 표시
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                count += 1
    
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            size = bfs(i, j)
            res += 1
            max_count = max(max_count, size)

print(res, max_count)