import sys
from itertools import combinations

input = sys.stdin.readline


N = int(input())

for _ in range(N):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    answer = 0
    for combi in combinations(words, 2):
        new_word = combi[0] + combi[1]
        if new_word == new_word[::-1]:
            answer = new_word
            break
        new_word = combi[1] + combi[0]
        if new_word == new_word[::-1]:
            answer = new_word
            break

    print(answer)
