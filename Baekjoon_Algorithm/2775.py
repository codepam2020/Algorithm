test_case = int(input())

for _ in range(test_case):
    floor = int(input())
    unit = int(input())
    f_list = [x for x in range(1, unit + 1)]
    for i in range(floor):
        for j in range(1, unit):
            f_list[j] += f_list[j - 1]
    print(f_list[-1])
