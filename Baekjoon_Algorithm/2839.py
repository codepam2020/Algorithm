from tracemalloc import stop


n = int(input())
result = -1

for i in reversed(range(int(n / 5) + 1)):
    rest = n - i * 5
    if rest % 3 == 0:
        result = i + int(rest / 3)
        break
    else:
        pass
print(result)
