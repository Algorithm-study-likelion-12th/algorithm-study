"""
입출력 예시
입력:
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

출력:
3
"""


def dfs(x, y):
    # y = 찾으려는 사람
    # x = 시작 사람
    stack = []
    visited = [0] * (node + 1)
    stack.append(x)

    # 나 = 1촌
    visited[x] = 1

    while stack:
        a = stack.pop()
        for i in graph[a]:
            if i == y:
                return visited[a]

            # 아직 안 계산한 사람이면
            if visited[i] == 0:
                stack.append(i)
                visited[i] = visited[a] + 1

    return -1


node = int(input())
people1, people2 = map(int, input().split())
edge = int(input())
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(people1, people2))
