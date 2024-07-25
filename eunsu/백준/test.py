data = list(input())
answer = []
tmp = []

for i in range(1, len(data) - 1):
    for j in range(i + 1, len(data)):
        first = data[0:i:-1]
        temp = first[::-1]
        print(f"first {first}, temp {temp}")
        second = data[i:j:-1]
        third = data[j : len(data) : -1]
        tmp.append(first + second + third)

for a in tmp:
    answer.append("".join(a))
print(sorted(answer)[0])
