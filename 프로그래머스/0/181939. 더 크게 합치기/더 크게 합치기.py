def solution(a, b):
    ab = a * 10**len(str(b)) + b
    ba = b * 10**len(str(a)) + a
    
    if ab >= ba:
        return ab
    else:
        return ba