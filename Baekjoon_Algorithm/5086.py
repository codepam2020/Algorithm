while True:
    a, b = map(int, input().split())
    if a == 0 & b == 0:
        True
        break
    elif a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
