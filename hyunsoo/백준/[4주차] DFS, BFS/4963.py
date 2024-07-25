# 백준 4963번 : 섬의 개수

# 0 = 바다
# 1 = 땅

def dfs(x, y, graph):
  if (x < 0) or  (x >= h) or (y < 0) or (y >= w):
    return True
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y, graph)
    dfs(x+1, y, graph)
    dfs(x, y-1, graph)
    dfs(x, y+1, graph)
    dfs(x-1, y-1, graph)
    dfs(x-1, y+1, graph)
    dfs(x+1, y-1, graph)
    dfs(x+1, y+1, graph)
    return True
  return False


while True :
  w, h = map(int, input().split())

  if (w == 0) and (h == 0):
    break
  graph = [list(map(int, input().split())) for _ in range(h)]

  result = 0
  for x in range(h):
    for y in range(w):
      if dfs(x, y, graph) == True:
        result += 1
  print(result)