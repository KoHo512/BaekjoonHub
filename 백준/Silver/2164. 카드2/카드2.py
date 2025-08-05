import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque(range(1, n + 1))

for _ in range(n - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])