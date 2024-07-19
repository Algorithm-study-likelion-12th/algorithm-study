from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_in_maze(a, b):
    if 0 <= a < N and 0 <= b < M:
        return True

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_in_maze(nx, ny) and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[N-1][M-1])
