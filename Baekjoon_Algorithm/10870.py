n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    for i in range(n - 1):
        result = a + b
        a = b
        b = result
    print(result)
