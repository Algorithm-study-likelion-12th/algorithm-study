# 백준 1012번 : 유기농 배추

# T = 테스트 케이스의 개수
## 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수 출력

# N = 배추밭의 세로길이
# M = 배추밭의 가로길이
# K = 배추가 심어져 있는 위치의 개수

def dfs(x, y, graph):
  if (x < 0) or (x >= N) or (y < 0) or (y >= M):
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y, graph)
    dfs(x+1, y, graph)
    dfs(x, y-1, graph)
    dfs(x, y+1, graph)
    return True
  return False

T = int(input())

for _ in range(T):
  N, M, K = map(int, input().split())
  
  graph = [[0]*M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    graph[x][y] = 1

  result = 0
  for n in range(N):
    for m in range(M):
      if dfs(n, m, graph) == True:
        result += 1
  
  print(result)