a, b = map(int, input().split())
result_list = list(range(a, b + 1))

for num in range(a, b + 1):
    if a == 1:
        result_list.remove(int(1))
    else:
        for i in range(2, num):
            if num % i == 0:
                result_list.remove(num)
                break
            else:
                pass


for i in range(len(result_list)):
    print(result_list[i])
