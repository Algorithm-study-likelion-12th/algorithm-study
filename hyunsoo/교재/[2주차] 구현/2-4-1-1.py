# 2-4-1-1. 상하좌우

# N = 공간의 크기 (1 <= N <= 100)

# L = 왼쪽으로 한 칸 이동 (Y - 1)
# R = 오른쪽으로 한 칸 이동 (Y + 1)
# U = 위로 한 칸 이동 (X - 1)
# D = 아래로 한 칸 이동 (X + 1)

X, Y = 1, 1
N = int(input())
route = list(input().split())

for n in range(N+1):
  r = route[n]
  if r == 'L':
    if Y == 1:
      continue
    else:
      Y -= 1
  if r == 'R':
    if Y == N:
      continue
    else:
      Y += 1
  if r == 'U':
    if X == 1:
      continue
    else:
      X -= 1
  if r == 'D':
    if X == N:
      continue
    else:
      X += 1

print(X, Y)