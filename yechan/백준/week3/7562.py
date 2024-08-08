#7562
import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")


def bfs(start_x, start_y, end_x, end_y, l):
  dx = [-2, -2, -1, -1, 1, 1, 2, 2]
  dy = [1, -1, 2, -2, 2, -2, 1, -1]
  queue = deque([(start_x, start_y, 0)])
  visited = [[False] * l for _ in range(l)]
  visited[start_x][start_y] = True
  while queue:
    x, y, cnt = queue.popleft()
    if x == end_x and y == end_y:
      return cnt
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny, cnt + 1))
  return -1


n = int(input())
for _ in range(n):
  l = int(input())
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())

  result = bfs(start_x, start_y, end_x, end_y, l)
  print(result)
