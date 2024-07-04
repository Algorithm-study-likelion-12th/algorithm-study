N, K = map(int, input().split())

cnt = 0
while(True):
    if N == 1:
        print(cnt)
        break
    rem = N % K
    for _ in range(rem):
        N -= 1
        cnt += 1
    if N >= K:
        N = N // K
        cnt += 1