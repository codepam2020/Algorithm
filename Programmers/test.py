a_list = [1, 1]
b_list = [1, 5]

a_total = sum(a_list)
b_total = sum(b_list)

all_total = a_total + b_total
count = 0


if all_total % 2 != 0:
    print(-1)
elif (max(a_list) > all_total / 2) or (max(b_list) > all_total / 2):
    print(-1)
else:
    while sum(a_list) != sum(b_list):
        if sum(a_list) > sum(b_list):
            b_list.append(a_list[0])
            a_list.remove(a_list[0])
            count += 1
        else:
            a_list.append(b_list[0])
            b_list.remove(b_list[0])
            count += 1
