n = int(input())
count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        print(i)
