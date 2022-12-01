a = list(input())
n = a.count(' ')
if a[0] == ' ' and a[len(a) - 1] == ' ':
    print(n - 1)
elif a[0] == ' ' and a[len(a) - 1] != ' ':
    print(n)
elif a[0] != ' ' and a[len(a) - 1] == ' ':
    print(n)
else:
    print(n + 1)