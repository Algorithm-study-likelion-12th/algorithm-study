# 2-4-1-2. 시각

N = int(input())
count1 = 0
count2 = 0

for n in range(N+1):
  if (n % 10 == 3) or (n // 10 == 3):
    count1 += 1
# print(count1)

for n in range(60):
  if (n % 10 == 3) or (n // 10 == 3):
    count2 += 1
# print(count2)

result = (N+1-count1)*(2*count2*60-count2*count2) + count1*60*60
# (((15 * 60) * 2 - (15 * 15)) * 5) + (60 * 60)
print(result)