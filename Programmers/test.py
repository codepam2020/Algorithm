<<<<<<< Updated upstream
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
=======
def solution(n, words):
    stack = [words[0]]
    answer = []
    for i in range(1, len(words)):
>>>>>>> Stashed changes

        if stack[-1][-1] != words[i][0]:
            answer.append(i + 1)
            break
=======
def solution(n, words):

    for i in words:
        print(i)
>>>>>>> Stashed changes

        elif words[i] in answer:
            answer.append(i + 1)
            break

        stack.append(words[i])

    return (answer[0] % n,)

<<<<<<< Updated upstream

answer = solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
)

print(answer)
=======
ans = solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
)

print(ans)
>>>>>>> Stashed changes
