import sys

input = sys.stdin.readline

n = int(input())

papers = [list(map(int, input().split())) for _ in range(n)]

white_paper = [[0] * 100 for _ in range(100)]

for paper in papers:
    for i in range(paper[0], paper[0] + 10):
        for j in range(paper[1], paper[1] + 10):
            white_paper[i][j] = 1


print(sum([sum(line) for line in white_paper]))