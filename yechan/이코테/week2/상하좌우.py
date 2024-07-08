# 상하좌우
import sys
# sys.stdin = open("input.txt", "rt")

row, column = 1, 1
n = int(input())
direction = list(input().split())
for d in direction:
    if (row == 1 and d == "U") or (row == n and d == "D") or (column == 1 and d == "L") or (column == n and d == "R"):
        continue
    if d == "L" : column -= 1
    if d == "R" : column += 1
    if d == "U" : row -= 1
    if d == "D" : row += 1
print(row, column)

