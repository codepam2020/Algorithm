n_test = int(input())

for i in range(n_test):
    a, b = map(int, input().split())
    x = a % 10
    if x == 1:
        ans = 1
    elif x == 5:
        ans = 5
    elif x == 0:
        ans = 10
    elif x == 6:
        ans = 6
print('hi')
