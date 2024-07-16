def is_in_maps(x, y):
    if 0 < x < N and 0 < y < M:
        return 1

N, M = map(int, input().split())
cur_x, cur_y, cur_dir = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
res = 1

while True:
    check = 0
    for i in range(3):
        cur_dir = (cur_dir + 3) % 4
        temp_x = cur_x + directions[cur_dir][0]
        temp_y = cur_y + directions[cur_dir][1]

        if maps[temp_x][temp_y] == 0:
            cur_x, cur_y = temp_x, temp_y
            res += 1
            maps[cur_x][cur_y] = -1
            check += 1
            break

    if check == 0:
        xx = cur_x-directions[cur_dir][0]
        yy = cur_y-directions[cur_dir][1]
        if is_in_maps(xx, yy):
            if maps[xx][yy] == 1:
                break
            else:
                cur_x = xx
                cur_y = yy
        else:
            break

print(res)
