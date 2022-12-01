n = int(input())
for _ in range(n):
    a, b = input().split()
    l = []
    for i in range(len(b)):
        l.append(b[i] * int(a))
    print(''.join(l))
