import sys
# sys.stdin = open("input.txt", "rt")
t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    odd = []
    even = []
    for i in range(n):
        if i % 2 == 0:
            odd.append(data[i])
        else:
            even.append(data[i])

    new = odd + even[::-1]
    new.append(odd[0])  

    sub = 0
    for i in range(n):
        temp = abs(new[i + 1] - new[i])
        sub = max(sub, temp)

    print(sub)
