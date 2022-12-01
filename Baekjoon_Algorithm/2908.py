a, b = map(list, input().split())
a_new = int(a[2] + a[1] + a[0])
b_new = int(b[2] + b[1] + b[0])
if a_new > b_new:
    print(a_new)
else:
    print(b_new)
