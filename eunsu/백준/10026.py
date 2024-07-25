from collections import deque

n = int(input())
picture = []
visited = []
result = [0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and picture[x][y] == picture[nx][ny]
                and not visited[nx][ny]
            ):
                visited[nx][ny] = 1
                q.append((nx, ny))


for _ in range(n):
    picture.append(list(input()))
    visited.append([0] * n)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result[0] += 1

for i in range(n):
    for j in range(n):
        if picture[i][j] == "G":
            picture[i][j] = "R"

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result[1] += 1

print(" ".join(map(str, result)))
