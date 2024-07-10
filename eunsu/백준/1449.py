n, l = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
count = 1
temp = num[0]
for i in range(n):
    if num[i] - temp > l - 1:
        count += 1
        temp = num[i]
print(count)
