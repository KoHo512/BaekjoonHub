def solution(code):
    mode = False
    ret = ''
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
        else:
            if (mode and i % 2 == 1) or (not mode and i % 2 == 0):
                ret += code[i]
    
    if len(ret) == 0:
        return "EMPTY"
    
    return ret
                