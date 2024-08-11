import sys
sys.setrecursionlimit(25000)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y <= N:
        return


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
counter = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dfs(i, j)
