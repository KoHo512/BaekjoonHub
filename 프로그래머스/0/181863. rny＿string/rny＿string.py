def solution(rny_string):
    return ''.join(["rn" if rny == "m" else rny for rny in rny_string])