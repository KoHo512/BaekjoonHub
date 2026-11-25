def solution(clothes):
    answer = 1
    closet = {}
    
    for n, t in clothes:
        if t in closet:
            closet[t] += 1
        else:
            closet[t] = 1
        
    for t in closet:
        answer *= closet[t] + 1
    
    return answer - 1