n = int(input())
num_list = list(map(int, input().split()))

result_list = []
for j in num_list:
    if j == 1:
        result_list.append(1)
    else:
        for k in range(2, j):
            if j % k == 0:
                result_list.append(j)
                break
            else:
                pass
print(n - len(result_list))
