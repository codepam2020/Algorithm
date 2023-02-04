def solution(n, words):
    wordsStack = [words[0]]
    ans = []

    for i in range(1, len(words)):
        if wordsStack[-1][-1] != words[i]:
            ans.append(i)


ans = solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
)

print(ans)
