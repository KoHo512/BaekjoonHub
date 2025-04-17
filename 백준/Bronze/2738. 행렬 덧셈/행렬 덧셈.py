import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] += matrix2[i][j]

for i in range(n):
    print(*matrix[i])