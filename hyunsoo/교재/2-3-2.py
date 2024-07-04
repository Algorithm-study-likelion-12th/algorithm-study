# 큰 수의 법칙

# N = 배열의 크기 (2 <= N <= 1,000)
# M = 숫자가 더해지는 횟수 (1 <= M <= 10,000)
# K = 연속해서 K번을 초과하여 더해질 수 없음 (1 <= K <= 10,000)

N, M, K = map(int, input().split())

if (2 <= N <=1000) and (1 <= M <= 10000) and (1 <= K <= 10000) and (K <= M):

  input_list = list(map(int, input().split()))
  sort_list = sorted(input_list)
  desc_list = list(reversed(sort_list))

  a = desc_list[0]
  b = desc_list[1]

  # data = list(map(int, input().split()))
  # data.sort()
  # first = data[n-1]
  # second = data[n-2]

  sum = (K * a + b) * (M // (K + 1)) + (M % (K + 1)) * a

  print(sum)

else:
  print("잘못된 입력")