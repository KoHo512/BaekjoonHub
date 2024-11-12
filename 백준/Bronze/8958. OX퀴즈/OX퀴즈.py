import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    results = input()
    score = 0
    correctCount = 0
    for result in results:
        if result == "O":
            correctCount += 1
            score += correctCount
        elif result == "X":
            correctCount = 0

    print(score)
