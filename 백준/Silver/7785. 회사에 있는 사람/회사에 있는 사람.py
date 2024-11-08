import sys

input = sys.stdin.readline

T = int(input())

peopleSet = set()

for _ in range(T):
    N = input().split()
    if N[1] == "enter":
        peopleSet.add(N[0])
    elif N[1] == "leave":
        peopleSet.discard(N[0])

peopleList = list(sorted(peopleSet, reverse=True))

for people in peopleList:
    print(people)
