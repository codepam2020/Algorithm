def solution(brown, yellow):
    size = [0, 0]

    if yellow == 1:
        size = [3, 3]

    for i in range(1, yellow // 2 + 1):
        if yellow // i == yellow / i:
            w, h = yellow / i + 2, i + 2

            if w * h - yellow == brown:
                size = [int(w), int(h)]
                break

        else:
            pass

    return size


ans = solution(8, 1)

print(ans)
