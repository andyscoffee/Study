def solution(participant, completion):
    hashdict = {}
    sumhash = 0

    for part in participant:
        hashdict[hash(part)] = part
        sumhash += hash(part)
    for comp in completion:
        sumhash -= hash(comp)

    return hashdict[sumhash]
