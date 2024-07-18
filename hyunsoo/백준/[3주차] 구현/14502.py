# 백준 14502번 : 연구소

# N = 세로 (3 <= N <= 8)
# M = 가로 (3 <= M <= 8)
# 0 = 빈 칸
# 1 = 벽
# 2 = 바이러스

from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def wall(cnt):
    if cnt == 3:
        virus()
        return

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 0:
                graph[n][m] = 1
                wall(cnt+1)
                graph[n][m] = 0

def virus():
    queue = deque()
    temp = copy.deepcopy(graph)

    for n in range(N):
        for m in range(M):
            if temp[n][m] == 2:
                queue.append((n, m))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    count(temp)

def count(temp):
    global safe
    count = 0
    for n in range(N):
        for m in range(M):
            if temp[n][m] == 0:
                count += 1

    safe = max(safe, count)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
safe = 0

wall(0)
print(safe)