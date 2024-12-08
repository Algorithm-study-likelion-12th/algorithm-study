# 2-6-4. 두 배열의 원소 교체

# n = 배열의 원소 개수
# k = 바꿔치기 연산 수행 횟수

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.reverse()
# B.sort(reverse=True)

for k in range(K):
  if A[k] < B[k]:
    A[k], B[k] = B[k], A[k]
  else:
    break

print(sum(A)) # 그럼 n은 왜 받은거지?