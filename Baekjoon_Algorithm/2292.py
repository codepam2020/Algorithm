n = int(input())
f = 1
p = 6
r = 1
if n == 1:
    print(1)
else:
    while True:
        f = f + p
        r += 1
        if n <= f:
            print(r)
            break
        p += 6
