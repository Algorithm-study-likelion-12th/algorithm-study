# 백준 18111번 : 마인크래프트

# N = 세로
# M = 가로
# B = 인벤토리

# 블록 제거 2초, 블록 쌓기 1초

N, M, B = map(int, input().split())
# for n in range(N):
#   for m in range(M):

data = []
for _ in range(N):
  data.append(map(int, input().split()))