a, b, l = map(int, input().split())
d = (l - b) / (a - b)
if d == int(d):
    print(int(d))
else:
    print(int(d) + 1)
