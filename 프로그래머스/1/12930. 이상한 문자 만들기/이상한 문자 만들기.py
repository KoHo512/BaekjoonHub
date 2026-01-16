def solution(s):
    answer = ''
    index = 0
    
    for ch in s:
        if ch == " ":
            answer += " "
            index = 0
            continue
        
        if index % 2 == 0:
            answer += ch.upper()
        else:
            answer += ch.lower()
            
        index += 1
            
    return answer