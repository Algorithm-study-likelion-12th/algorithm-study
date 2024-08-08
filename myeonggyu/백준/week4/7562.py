from collections import deque

def move_knight(x, y):
    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, 2, 2, 1, -1, -2, -2]

    queue = deque([(x, y)])
    while queue:
        pos = queue.popleft()
        if pos[0] == end[0] and pos[1] == end[1]:
            return chess[pos[0]][pos[1]]

        for i in range(8):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[pos[0]][pos[1]] + 1
                queue.append((nx, ny))


N = int(input())
for _ in range(N):
    I = int(input())
    chess = [[0] * I for _ in range(I)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    res = move_knight(start[0], start[1])
    print(res)
