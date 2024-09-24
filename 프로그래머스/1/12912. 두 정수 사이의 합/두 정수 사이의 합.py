def solution(a, b):
    ab = 1 if a < b else -1
    return sum([i for i in range(a, b + ab, ab)])
        