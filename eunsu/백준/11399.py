n = int(input())
num = list(map(int, input().split()))
num.sort()
result, temp = 0, 0
for i in range(n):
    result += num[i] + temp
    temp += num[i]
print(result)
