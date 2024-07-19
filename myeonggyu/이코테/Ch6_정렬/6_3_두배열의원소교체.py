N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

idx = 0
while idx < K and A[idx] < B[idx]:
    A[idx], B[idx] = B[idx], A[idx]
    idx += 1

print(sum(A))
