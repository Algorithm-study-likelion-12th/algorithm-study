# 백준 2960번 : 에라토스테네스의 체

N, K = map(int, input().split())
data = list(range(2, N+1))

while K > 0:
  P = data[0]
  lis = list(range(P, N+1, P))
  for n in range(len(lis)):
    if lis[n] in data:
      if K == 1:
        print(lis[n])
      else:
        data.remove(lis[n])
      K -= 1
    else:
      continue