# 1012
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())


def dfs(x, y, data):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x, y - 1, data)
        dfs(x, y + 1, data)
        dfs(x - 1, y, data)
        dfs(x + 1, y, data)
        return True
    return False


for _ in range(T):
    # 기본 세팅
    res = 0
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1
    # 기능
    for i in range(n):
        for j in range(m):
            if dfs(i, j, data) == True:
                res += 1
    print(res)
