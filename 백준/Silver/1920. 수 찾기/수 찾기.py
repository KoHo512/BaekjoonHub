import sys
input = sys.stdin.readline

N = int(input())
numN = set(map(int, input().split()))

M = int(input())
numM = list(map(int, input().split()))

for num in numM:
    if num in numN:
        print(1)
    else:
        print(0)