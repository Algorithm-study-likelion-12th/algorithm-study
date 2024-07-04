N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

count, result = 0, 0

# 반복문을 사용해서 다음처럼 진행하면 시간 초과가 발생할 수 있음.
# for _ in range(M):
#     if count == K:
#         count = 0
#         result += data[-2]
#         continue
#     count += 1
#     result += data[-1]

# 가장 큰 수와 두 번째로 큰 수가 각각 몇 번씩 더해지는지 파악 후 반복문 없이 해결 가능.
first = data[-1]
second = data[-2]

result += first * ((M // (K + 1)) * K + M % (K + 1))
result += second * (M // (K + 1))

print(result)