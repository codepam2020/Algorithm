a = int(input())
b = list(map(int, str(input())))
sum = 0
for i in range(a):
    sum += b[i]
print(sum)