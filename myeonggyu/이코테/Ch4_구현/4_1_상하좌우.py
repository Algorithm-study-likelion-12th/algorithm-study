import sys

input = sys.stdin.readline
N = int(input())
data = list(input().split())

pos = [0, 0]

for move in data:
    if move == 'U' and pos[0] - 1 >= 0:
        pos[0] -= 1
    elif move == 'R' and pos[1] + 1 < N:
        pos[1] += 1
    elif move == 'D' and pos[0] + 1 < N:
        pos[0] += 1
    elif move == 'L' and pos[1] - 1 >= 0:
        pos[1] -= 1

print(pos[0]+1, pos[1]+1)
