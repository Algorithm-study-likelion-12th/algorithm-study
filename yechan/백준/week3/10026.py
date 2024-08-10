import sys

sys.setrecursionlimit(10000)
# sys.stdin = open("input.txt", "rt")
n = int(input())
graph = [list(input()) for _ in range(n)]
graph_color = [row[:] for row in graph]
normal_result = 0


def dfs(x, y, color, graph):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if graph[x][y] != color:
        return
    graph[x][y] = '0'

    dfs(x - 1, y, color, graph)
    dfs(x + 1, y, color, graph)
    dfs(x, y - 1, color, graph)
    dfs(x, y + 1, color, graph)


def count_areas(graph):
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != '0':
                dfs(i, j, graph[i][j], graph)
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph_color[i][j] == "G":
            graph_color[i][j] = "R"

normal_result = count_areas([row[:] for row in graph])
colorblind_result = count_areas(graph_color)

print(normal_result, colorblind_result)
