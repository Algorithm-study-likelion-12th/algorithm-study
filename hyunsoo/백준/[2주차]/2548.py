# 백준 2548번 : 대표 자연수
# N = 자연수의 개수 (1 <= N <= 20,000)
# 대표 자연수가 두 개 이상일 경우 그 중 제일 작은 것을 출력

N = int(input())
num = list(map(int, input().split()))
num.sort()

if N % 2 == 0:
  print(num[N // 2 - 1])

else:
  print(num[N // 2])