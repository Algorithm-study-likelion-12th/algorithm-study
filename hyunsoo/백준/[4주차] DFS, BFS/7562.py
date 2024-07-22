# 백준 7562번 : 나이트의 이동
# T = 테스트 케이스
# L = 체스판 한 변의 길이
# BFS

from collections import deque

# dx = [-1, -2, -2, -1, 1, 2, 2, 1]
# dy = [-2, -1, 1, 2, -2, -1, 1, 2]
d = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)]


def bfs(start_x, start_y, end_x, end_y, graph):
  queue = deque([(start_x, start_y)])
  
  while queue:
    x, y = queue.popleft()
    for dx, dy in d:
      nx, ny = x + dx, y + dy


      if (nx < 0) or (nx >= L) or (ny < 0) or (ny >= L):
        continue

      if (x, y) == (end_x, end_y):
        return graph[x][y]

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

T = int(input())

for _ in range(T):
  L = int(input())

  chess = [[0]*L for _ in range(L)]

  # start
  x1, y1 = map(int, input().split())
  # end
  x2, y2 = map(int, input().split())

  result = bfs(x1, y1, x2, y2, chess)
  print(result)