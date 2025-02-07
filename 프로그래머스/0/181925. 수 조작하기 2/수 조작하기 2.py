def solution(numLog):
    answer = ''
    
    for i in range(len(numLog) - 1):
        val = numLog[i + 1] - numLog[i]
        if val == 1:
            answer += 'w'
        elif val == -1:
            answer += 's'
        elif val == 10:
            answer += 'd'
        elif val == -10:
            answer += 'a'
        
    return answer