import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    check = []
    answer = ""
    parenthesis = input()

    for ps in parenthesis:
        if ps == "(":
            check.append(ps)
        elif ps == ")":
            if not check:
                print("NO")
                break
            
            check.pop()
    else:
        if check:
            print("NO")
        else:
            print("YES")