def move(choice, now):
    tmp = now.copy()
    if choice == "L":
        now[1] -= 1
    elif choice == "R":
        now[1] += 1
    elif choice == "U":
        now[0] -= 1
    elif choice == "D":
        now[0] += 1

    if now[0] < 1 or now[1] < 1 or now[0] > n or now[1] > n:
        return tmp
    else:
        return now


now = [1, 1]
n = int(input())
choice = list(input().split())

for i in range(n + 1):
    now = move(choice[i], now)

print(f"{now[0]} {now[1]}")
