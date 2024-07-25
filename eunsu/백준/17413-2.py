i = 0
start = 0
data = list(input())

while i < len(data):
    if data[i] == "<":
        i += 1
        while data[i] != ">":
            i += 1
        # <까지는 그대로 넣어주기 위해
        i += 1
    elif data[i].isalnum():
        start = i
        while i < len(data) and data[i].isalnum():
            i += 1
        temp = data[start:i]
        temp.reverse()
        data[start:i] = temp

    # 공백인 경우
    else:
        i += 1  # 그냥 증가

print("".join(data))
