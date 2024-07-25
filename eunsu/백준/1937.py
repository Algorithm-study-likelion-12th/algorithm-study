"""
    사용 알고리즘
    - dfs
    - dp
        각 좌표의 이동 가능 최대 수를 기록하기 위해 dp를 사용

    실패 케이스
    - BFS로 문제를 풀기 시작했지만, 시간 초과


    개념 정리

    BFS:
    시작 노드에서 가까운 노드부터 차례대로 탐색하는 방식입니다.
    최단 경로 문제, 최소 비용 문제 등에 적합합니다.
    큐 자료구조를 사용하여 구현합니다.
    
    DFS:
    시작 노드에서 가능한 한 깊이 내려가면서 탐색하는 방식입니다.
    경로 찾기, 연결 요소 찾기 등에 적합합니다.
    스택 자료구조를 사용하여 구현합니다.
    
    DP :
    DP는 복잡한 문제를 작은 하위 문제로 나누어 해결하는 방법입니다.
    이전에 계산한 결과를 저장하여 중복 계산을 방지합니다.
    최적화 문제, 재귀적 문제 등에 적합합니다.

    BFS: 최단 경로, 최소 비용 문제
    DFS: 경로 찾기, 연결 요소 찾기
    DP: 최적화 문제, 재귀적 문제

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    # 이미 계산한 최대 이동 가능 거리는 저장한 값 반환
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
dp = [[0] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
