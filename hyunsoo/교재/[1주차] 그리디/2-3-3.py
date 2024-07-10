# 숫자 카드 게임

# N = 행
# M = 열

N, M = map(int, input().split())

result = []

for n in range(N):
  data = list(map(int, input().split()))
  result.append(min(data))

print(max(result))