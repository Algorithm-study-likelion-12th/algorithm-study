n = int(input())
num = list(map(int, input().split()))
num.sort(reverse=True)
min_result = [-1, 99999999999]  # 대표 수, 차이의 전체 합
flag = False

for i in range(n):
    result = 0
    for j in range(n):
        result += abs(num[i] - num[j])
        if result > min_result[1]:
            flag = False
            break
        flag = True
    if flag:
        min_result[0] = num[i]
        min_result[1] = result

print(min_result[0])
