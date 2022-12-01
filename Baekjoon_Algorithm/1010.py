n_test = int(input())

for i in range(n_test):
    a, b = map(int, input().split())
    child = 1
    parent = 1
    for x in range(b - a + 1, b + 1):
        child = child * x
    for y in range(1, a + 1):
        parent = parent * y
    print(int(child / parent))
