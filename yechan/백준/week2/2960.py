import sys
# sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

a = [i for i in range(2, n+1)]
cnt = 0
while a and cnt != k:
    num = min(a)
    a.remove(num)
    res = num
    cnt += 1
    to_remove = []  # 제거할 원소를 저장할 리스트
    for i in a:
        if i % num == 0:
            to_remove.append(i)
            res = i
            cnt += 1
            if cnt == k:  # k번째 소수를 찾으면 종료
                break
    for i in to_remove:
        a.remove(i)
if cnt == k:
    print(res)
