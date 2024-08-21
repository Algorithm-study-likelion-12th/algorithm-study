# import sys
# sys.setrecursionlimit(250000)
# from collections import deque
#
# def bfs(x, y):
#     if counter[x][y] != 0:
#         return
#
#     queue = deque([(x, y, 1)])
#     while queue:
#         xx, yy, t = queue.popleft()
#         if t > counter[xx][yy]:
#             counter[xx][yy] = t
#         else:
#             continue
#         for dx, dy in d:
#             nx = xx + dx
#             ny = yy + dy
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#             if forest[nx][ny] > forest[xx][yy]:
#                 queue.append((nx, ny, t + 1))
#
#
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# counter = [[0] * N for _ in range(N)]
# d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# for i in range(N):
#     for j in range(N):
#         bfs(i, j)
#
# res = max(map(max, counter))
# print(res)

import sys
sys.setrecursionlimit(250000)

def dfs(x, y, cnt):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if forest[nx][ny] > forest[x][y] and cnt + 1 > counter[nx][ny]:
            dfs(nx, ny, cnt + 1)



N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
counter = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        dfs(i, j, 1)

res = max(map(max, counter))
print(res)
