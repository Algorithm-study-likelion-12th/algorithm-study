# 백준 10866번 : 덱

# 주어지는 명령의 수
N = int(input())
deque = []

for _ in range(N):
  n = input().split()
  if n[0] == 'push_front':
    deque.insert(0, n[1])
  elif n[0] == 'push_back':
    deque.append(n[1])
  elif n[0] == 'pop_front':
    if len(deque) > 0:
      x = deque.pop(0)
      print(x)
    else:
      print(-1)
  elif n[0] == 'pop_back':
    if len(deque) > 0:
      x = deque.pop(-1)
      print(x)
    else:
      print(-1)
  elif n[0] == 'size':
    print(len(deque))
  elif n[0] == 'empty':
    if len(deque) == 0:
      print(1)
    else:
      print(0)
  elif n[0] == 'front':
    if len(deque) > 0:
      print(deque[0])
    else:
      print(-1)
  elif n[0] == 'back':
    if len(deque) > 0:
      print(deque[-1])
    else:
      print(-1)