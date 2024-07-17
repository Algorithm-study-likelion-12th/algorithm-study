# 게임 개발
import sys
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
x, y, d = map(int, input().split())
region = []
for i in range(n):
    region.append(list(map(int, input().split())))
region[x][y] = 2
cnt = 1
 
# 북, 동, 남, 서
dx = [0, -1, 0, 1] 
dy = [1, 0, -1, 0]

# 왼쪽으로 돌기...
def turn_left(d):
    return (d+3) % 4

while(True):
    moved = False
    for _ in range(4):
        d = turn_left(d)
        tx = x + dx[d]
        ty = y + dy[d]
        if 0 <= tx < n and 0 <= ty < m and region[tx][ty] == 0:
            region[tx][ty] = 2 # 가본 칸을 2로 설정.
            x, y = tx, ty
            cnt += 1
            moved = True
            break

    if not moved:
        tx = x - dx[d]
        ty = y - dy[d]
        if tx < 0 or tx >= n or ty < 0 or ty >= n or region[tx][ty] == 1:
            print(cnt)
            break
        x, y = tx, ty

