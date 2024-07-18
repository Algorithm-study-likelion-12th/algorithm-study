# 2-5-3. 음료수 얼려먹기
# DFS

# N X M 크기의 얼음틀
# 0 = 구멍이 뚫린 부분 (상하좌우로 붙어있는 경우 연결된 것으로 간주)
# 1 = 칸막이가 존재하는 부분

# N = 세로 길이
# M = 가로 길이

N, M = map(int, input().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

def dfs(x, y, graph):
  if (x < 0) or (x >= N) or (y < 0) or (y >= M):
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x, y-1, graph) # 상
    dfs(x, y+1, graph) # 하
    dfs(x-1, y, graph) # 좌
    dfs(x+1, y, graph) # 우
    return True
  return False

result = 0
for n in range(N):
  for m in range(M):
    if dfs(n, m, graph) == True:
      result += 1

print(result)