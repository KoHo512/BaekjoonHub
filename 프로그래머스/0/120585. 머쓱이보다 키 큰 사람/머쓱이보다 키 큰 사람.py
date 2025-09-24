def solution(array, height):
    return sum(1 if h > height else 0 for h in array)