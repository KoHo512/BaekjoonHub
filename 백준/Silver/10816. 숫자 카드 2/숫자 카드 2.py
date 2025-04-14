import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards_dict = {}

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

M = int(input())
cards = list(map(int, input().split()))

# print(" ".join([str(cards_dict.get(card, 0)) for card in cards]))

answer = [cards_dict.get(card, 0) for card in cards]
print(*answer, sep=" ")