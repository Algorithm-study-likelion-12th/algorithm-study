import sys
from collections import deque

sys.setrecursionlimit(10000)

#sys.stdin = open("input.txt", "rt")
n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 관계 입력받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 관계


def bfs(start, end):
    q = deque([(start, 0)])  # (노드, 촌수)
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, chon = q.popleft()

        if now == end:
            return chon

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, chon + 1))

    return -1  # 관계가 없는 경우


result = bfs(a, b)
print(result)
