n = int(input())
for _ in range(n):
    w = input()
    for i in range(1, len(w)):
        if w.find(w[i - 1]) > w.find(w[i]):
            n -= 1
            break
print(n)
