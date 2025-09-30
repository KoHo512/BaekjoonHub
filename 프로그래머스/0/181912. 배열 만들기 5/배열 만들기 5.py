def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        number = int(str(intStr)[s: s + l])
        if number > k:
            answer.append(number)
            
    return answer