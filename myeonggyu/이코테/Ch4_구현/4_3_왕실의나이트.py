user_input = list(input())

row = int(user_input[1]) - 1
col = int(ord(user_input[0])) - int(ord('a'))
move = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [-1, -2], [1, -2]]

cnt = 0
for i in move:
    temp = [row+i[0], col+i[1]]
    if 0 <= temp[0] < 8 and 0 <= temp[1] < 8:
        cnt += 1

print(cnt)
