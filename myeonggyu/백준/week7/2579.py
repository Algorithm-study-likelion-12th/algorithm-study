# 2579 계단 오르기

import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
stairs.insert(0, 0)
dp = [0] * 301

if N <= 2:
    print(sum(stairs))
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[N])