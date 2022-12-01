scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
list_input = list(map(int, input().split()))

sum = 0
hacker = 0

for i in range(9):
    sum += list_input[i]

    if list_input[i] > scores[i]:
        hacker += 1

if hacker >= 1:
    print('hacker')
else:
    print('draw' if sum >= 100 else 'none')
