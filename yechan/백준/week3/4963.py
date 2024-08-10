# 4963
import sys

#sys.stdin = open("input.txt", "rt")

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    data = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        elif data[x][y] == 1:
            data[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y - 1)
            dfs(x - 1, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y + 1)
            return True

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)
