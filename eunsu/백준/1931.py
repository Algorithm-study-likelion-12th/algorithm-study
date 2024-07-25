reservation = []
n = int(input())
for i in range(n):
    reservation.append(list(map(int, input().split())))
reservation.sort(key=lambda x: (x[1], x[0]))

result = 0
end = 0

for i in range(n):
    if reservation[i][0] >= end:
        result += 1
        end = reservation[i][1]

print(result)
