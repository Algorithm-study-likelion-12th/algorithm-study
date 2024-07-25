inputs = input()
reversed_words = []


def find_blank(simple, reversed_simple_words):
    reversed_simple_words = []
    for word in simple:
        reversed_word = "".join(reversed(word))
        reversed_simple_words.append(reversed_word)
    reversed_words.append(" ".join(reversed_simple_words))
    return reversed_words


if "<" in inputs:
    remember = []
    start, end = None, None

    for i in range(len(inputs)):
        if inputs[i] == "<":
            start = i
        elif inputs[i] == ">":
            end = i
            remember.append((start, end))
            start, end = None, None
            continue_flag = False
        else:
            continue_flag = True
    for i in range(len(remember) + int(continue_flag)):
        if continue_flag and i == len(remember) + int(continue_flag) - 1:
            if " " in inputs[remember[i - 1][1] + 1 :]:
                reversed_simple_words = inputs[remember[i - 1][1] + 1 :].split()
                reversed_words = find_blank(simple, reversed_simple_words)
            else:
                reversed_word = "".join(reversed(inputs[remember[i - 1][1] + 1 :]))
                reversed_words.append(reversed_word)
            continue

        reversed_words.append(inputs[remember[i][0] : remember[i][1] + 1])

        if i != len(remember) - 1:
            if " " in inputs[remember[i][1] + 1 : remember[i + 1][0]]:
                simple = inputs[remember[i][1] + 1 : remember[i + 1][0]].split()
                reversed_words = find_blank(simple, simple)
            else:
                reversed_word = "".join(
                    reversed(inputs[remember[i][1] + 1 : remember[i + 1][0]])
                )
                reversed_words.append(reversed_word)
    print("".join(reversed_words))
else:
    simple = inputs.split()
    reversed_words = find_blank(simple, simple)
    print(" ".join(reversed_words))
