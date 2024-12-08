# 2-6-3. 성적이 낮은 순서로 학생 출력하기

def setting(data):
  return data[1]

# 학생의 수
N = int(input())

student_score = []
for _ in range(N):
  n = input().split()
  student_score.append((n[0], int(n[1])))

result = sorted(student_score, key=setting)

for i in range(N):
  print(result[i][0], end =' ')