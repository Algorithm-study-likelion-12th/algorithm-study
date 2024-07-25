n, m, b = map(int, input().split())
block = []
for _ in range(n):
    block.append([int(x) for x in input().split()])

time = int(1e9)
high = 0

for i in range(257):
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    if use_block > take_block + b:
        continue

    count = take_block * 2 + use_block

    if count <= time:
        time = count
        high = i

print(time, high)
