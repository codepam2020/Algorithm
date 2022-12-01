n, m = map(int, input().split())
c = list(map(int, input().split()))
b = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = c[i] + c[j] + c[k]
            if a > m:
                pass
            else:
                b = max(b, a)
print(b)