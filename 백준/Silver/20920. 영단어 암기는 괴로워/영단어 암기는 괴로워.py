import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

counter = Counter(words)
results = sorted(set(words), key=lambda word: (-counter[word], -len(word), word))

for word in results:
    if len(word) >= m:
        print(word)