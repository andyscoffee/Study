# Summer/Winter Coding(~2018) 영어 끝말잇기 (난이도 2)
def solution(n, words):
    answer = []
    word = dict()
    for i in range(len(words)):
        if i == 0:
            word[words[i]] = 1
            continue
        if words[i][0] == words[i-1][-1] and words[i] not in word.keys():
            word[words[i]] = 1
        else:
            answer.append((i % n) + 1)
            answer.append((i//n)+1)
            break
    if len(answer) == 0:
        return [0, 0]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "e", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ['qwe', 'eqwe', 'eqwe']), "1,2")
print(solution(2, ["land", "dream", "mom", "mom", "ror"]), "2,2")
print(solution(2, ["land", "dream", "mom", "mom"]), "2,2")
print(solution(3, ["qwe", "eqwe", "eqwe"]), "3,1")
print(solution(2, ["qwe", "eqwe", "eqqwe", "eqqwe"]), "2,2")
print(solution(2, ["qwe", "qwe"]), "2,1")
print(solution(2, ["ewe", "ewe"]), "2,1")
