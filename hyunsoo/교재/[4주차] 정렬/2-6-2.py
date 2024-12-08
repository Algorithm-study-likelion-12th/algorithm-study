# 2-6-2. 위에서 아래로
# 수열을 내림차순으로 정렬하는 프로그램

# 수열에 속해 있는 수의 개수
N = int(input())

n = [int(input()) for _ in range(N)]

result = list(reversed(sorted(n)))
# result = sorted(n, reverse=True)

for i in range(N):
  print(result[i], end =' ')