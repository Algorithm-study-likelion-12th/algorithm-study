n = int(input())
num = list(map(int, input().split()))
num.sort()
min = 9999999999
result = []
start = 0
end = n - 1
while start < end:
    temp = num[start] + num[end]
    if min > abs(temp):
        min = abs(temp)
        result = [num[start], num[end]]
    if temp > 0:
        end -= 1
    else:
        start += 1
result.sort()
print(result[0], result[1])
