def solution(s):
    n = 0
    
    for a in s:
        if a == "(":
            n += 1
        else:
            if n == 0:
                return False
            n -= 1
        
    if n == 0:
        return True
    return False