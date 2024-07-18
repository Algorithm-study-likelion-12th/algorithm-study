# 백준 11399번 : ATM

N = int(input())
time = list(map(int, input().split()))

time.sort()

sum = 0

for n in range(N):
  nsum = 0
  for nn in range(n + 1):
    nsum += time[nn]
  sum += nsum

print(sum)