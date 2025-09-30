def solution(number):
    # return int(number) % 9
    return sum(int(n) for n in number) % 9