def solution(s):
    num_p = num_y = 0
    
    for a in s:
        if a == 'p' or a == 'P':
            num_p += 1
        elif a == 'y' or a == 'Y':
            num_y += 1
    
    if num_p == num_y:
        return True
    return False
        