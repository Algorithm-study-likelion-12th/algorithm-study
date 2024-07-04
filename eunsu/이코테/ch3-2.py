# 큰 수의 법칙

import time

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
first = numbers[-1]
second = numbers[-2]
result = 0
start_time = time.time()
while True:
    if m == 0:
        break
    if m < k:
        result += first * m
        break
    else:
        result += first * k + second
        m -= k + 1

print(result)

# 코드 수정본
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[-1]
second = numbers[-2]
result = 0

# TODO 한글 변수명 삭제
몫, 나머지 = divmod(m, k + 1)
result = 몫 * (first * k + second) + 나머지 * first
print(result)
