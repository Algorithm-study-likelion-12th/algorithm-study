import copy
from collections import deque

result = -1


def find_virus(n, m, temp_map):
    virus = deque()
    for i in range(n):
        for k in range(m):
            if temp_map[i][k] == 2:
                virus.append((i, k))
    return virus


def spread_virus(virus, temp_map, n, m):
    # 바이러스가 퍼질 수 있는 위치 위, 아래, 왼쪽, 오른쪽
    location = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while virus:
        x, y = virus.popleft()

        for i in range(4):
            # 바이러스가 이동할 위치를 담고 있는 변수 move_@
            move_x = x + location[i][0]
            move_y = y + location[i][1]

            if (0 <= move_x < n) and (0 <= move_y < m):
                if temp_map[move_x][move_y] == 0:
                    temp_map[move_x][move_y] = 2
                    virus.append((move_x, move_y))
    return temp_map


def count_zero(temp_map, n, m):
    count = 0
    for i in range(n):
        for k in range(m):
            if temp_map[i][k] == 0:
                count += 1
    return count


def bfs(map, n, m):
    temp_map = copy.deepcopy(map)
    virus = find_virus(n=n, m=m, temp_map=temp_map)
    temp_map = spread_virus(virus=virus, temp_map=temp_map, n=n, m=m)
    count = count_zero(temp_map=temp_map, n=n, m=m)

    # 전역변수로 선언
    global result
    result = max(result, count)


def build_wall(map, count, n, m):
    if count == 3:
        bfs(map=map, n=n, m=m)
        return
    for i in range(n):
        for k in range(m):
            if map[i][k] == 0:
                map[i][k] = 1
                build_wall(map=map, count=count + 1, n=n, m=m)
                map[i][k] = 0


def start():
    n, m = map(int, input().split())
    origin_map = []
    for i in range(n):
        origin_map.append(list(map(int, input().split())))
    build_wall(map=origin_map, count=0, n=n, m=m)
    print(result)


start()
