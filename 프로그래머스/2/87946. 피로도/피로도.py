from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for permutation in permutations(dungeons):
        count = 0
        tmpK = k
        for dungeon in permutation:
            if tmpK >= dungeon[0]:
                count += 1
                tmpK -= dungeon[1]
                answer = max(answer, count)
    
    return answer