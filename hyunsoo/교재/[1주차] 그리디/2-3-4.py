# 1이 될 때까지

# N에서 1을 빼거나 N을 K로 나눔

N , K = map(int, input().split())

count = N % K

while N > 1:
  N //= K
  count += 1

print(count)