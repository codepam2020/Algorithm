pn = int(input())  # problem number

for i in range(pn):
    ans = input()
    li = list(ans)
    sum = 0
    sc = 1  # score
    for i in li:
        if i == 'O':
            sum += sc
            sc += 1
        else:
            sc = 1
    print(sum)
