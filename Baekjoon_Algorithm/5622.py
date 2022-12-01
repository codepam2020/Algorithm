input = input()
time = 0
li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in range(len(input)):
    for j in li:
        if input[i] in j:
            time += li.index(j) + 3
print(time)