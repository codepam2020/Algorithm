def solution(s):
    word = s
    ans = 0
    while True:
        afterWord = word
        for i in range(1, len(afterWord)):
            if afterWord[i - 1] == afterWord[i]:
                afterWord = afterWord[: i - 1] + afterWord[i + 1 :]
                break

        if afterWord == word:
            if afterWord == "":
                ans = 1
            else:
                ans = 0
            break

        else:
            word = afterWord
    return ans


answer = solution(15)

print(answer)
