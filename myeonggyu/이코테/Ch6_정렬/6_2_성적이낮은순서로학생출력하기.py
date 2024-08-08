N = int(input())
data = []
for _ in range(N):
    line = input().split()
    data.append((line[0], int(line[1])))

data.sort(key=lambda x: x[1])

for student in data:
    print(student[0], end=' ')
