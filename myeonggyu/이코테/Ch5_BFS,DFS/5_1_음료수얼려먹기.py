from collections import deque

N, M = map(int, input().split())
icebox = [list(map(int, input())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def is_in_icebox(nx, ny):
    if 0 <= nx < N and 0 <= ny < M:
        return True

for i in range(N):
    for j in range(M):
        if icebox[i][j] == 0:
            queue = deque([(i, j)])
            icebox[i][j] = 1
            cnt += 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_in_icebox(nx, ny) and icebox[nx][ny] == 0:
                        queue.append((nx, ny))
                        icebox[nx][ny] = 1

print(cnt)
