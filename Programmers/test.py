<<<<<<< Updated upstream
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
=======
def solution(n, words):

    for i in words:
        print(i)
>>>>>>> Stashed changes

        else:
            word = afterWord
    return ans

<<<<<<< Updated upstream

answer = solution(15)

print(answer)
=======
ans = solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
)

print(ans)
>>>>>>> Stashed changes
