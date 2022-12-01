n = int(input())

for i in range(1, n + 1):
    d = list(map(int, str(i)))
    s = i + sum(d)
    if (s == n):
        print(i)
        break
    elif i == n:
        print(0)