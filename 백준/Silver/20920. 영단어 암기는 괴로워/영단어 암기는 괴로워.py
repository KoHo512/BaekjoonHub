import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

words = []

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

counter = Counter(words)

def sort_word(word):
    return -counter[word], -len(word), word

words = sorted(set(words), key=sort_word)

for word in words:
    print(word)