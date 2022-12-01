n_case = int(input())

for i in range(n_case):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n_count = int(input())
    for k in range(n_count):
        x, y, r = map(int, input().split())
        d1 = (((x1 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
        d2 = (((x2 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            count += 1

    print(count)

