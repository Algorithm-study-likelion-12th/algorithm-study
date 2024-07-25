word = list(input())
case_list = []
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        first.reverse()

        second = word[i:j]
        second.reverse()
        third = word[j:]
        third.reverse()

        case_list.append("".join(first + second + third))
result = min(case_list)
print(result)
