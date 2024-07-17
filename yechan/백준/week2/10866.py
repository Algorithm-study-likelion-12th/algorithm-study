import sys
# sys.stdin = open("input.txt", "rt")
from collections import deque

n = int(input())
data = [list(input().split()) for _ in range(n)]
deq = deque()

for i in range(n):
    if data[i][0] == "push_back":
        deq.append(data[i][1])
    elif data[i][0] == "push_front":
        deq.appendleft(data[i][1])
    elif data[i][0] == "pop_front":
        if deq:
            temp = deq.popleft()
            print(temp)
        else:
            print(-1)
    elif data[i][0] == "pop_back":
        if deq:
            temp = deq.pop()
            print(temp)
        else:
            print(-1)
    elif data[i][0] == "size":
        print(len(deq))
    elif data[i][0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif data[i][0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif data[i][0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
