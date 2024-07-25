import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        (x, y) = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    que.append((nx, ny))
                    visited[nx][ny] = True


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit()
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1
    print(cnt)
