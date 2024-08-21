N = int(input())
class_time = [list(map(int, input().split())) for _ in range(N)]
class_time.sort(key=lambda x:(x[0],x[1]))
res = [[[0, 0]]]

for data in class_time:
    create = True
    for res_in in res:
        print(res_in)
        if res_in[-1][1] < data[0]:
            res.append(data)
            create = False
    if create:
        res.append([data])

print(len(res))
