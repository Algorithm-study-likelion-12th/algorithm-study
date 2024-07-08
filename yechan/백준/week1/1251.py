# 1251
import sys
# sys.stdin = open("input.txt", "rt")
data = list(input())
answer = []
tmp = []

for i in range(1, len(data)-1):
    for j in range(i+1, len(data)):
        first = data[0:i]
        second = data[i:j]
        third = data[j:len(data)]
        first.reverse()
        second.reverse()
        third.reverse()
        tmp.append(first+second+third)

for a in tmp:
    answer.append(''.join(a))
print(sorted(answer)[0])