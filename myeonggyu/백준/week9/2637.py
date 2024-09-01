# 2637 장난감 조립

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
component = [[0] * (N + 1) for _ in range(N + 1)]

M = int(input().rstrip())
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[a] += 1

def topology_sort():
    q = deque()

    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
            component[i][i] = 1
            indegree[i] -= 1

    while q:
        now = q.popleft()
        for i in range(1, N + 1):
            for j in graph[i]:
                if now == j[0]:
                    indegree[i] -= 1
                    for k in range(1, N + 1):
                        component[i][k] += component[j[0]][k] * j[1]
            if not indegree[i]:
                q.append(i)
                indegree[i] -= 1

topology_sort()
for i in range(1, N + 1):
    if component[N][i]:
        print(i, component[N][i])