import sys
# sys.stdin = open("input.txt", "rt")

def reverse_words(s):
    result = []
    word = []
    in_tag = False

    for char in s:
        if char == '<' :
            if word:
                result.append(''.join(reversed(word)))
                word = []
            #열어주고
            in_tag = True
            result.append(char)
        elif char == '>':
            #닫아주고
            in_tag = False
            result.append(char)
        elif in_tag:
            result.append(char)
        elif char.isalnum():
            word.append(char)
        else:
            if word:
                result.append(''.join(reversed(word)))
                word = []
            result.append(char)
        
    if word:
        result.append(''.join(reversed(word)))

    return ''.join(result)



s = input().rstrip()

print(reverse_words(s))
