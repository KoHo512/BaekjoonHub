def solution(input_string):
    answer = ''
    check_string = 'N'
    
    for c in input_string:
        if c in check_string and c != check_string[-1] and c not in answer:
            answer += c
            
        if c is not check_string[-1]: 
            check_string += c        
    
    return ''.join(sorted(answer)) if answer else "N"