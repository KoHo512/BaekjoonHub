def solution(clothes):
    closet = {}
    
    for c, t in clothes:
        if t in closet:
            closet[t].append(c)
        else:
            closet[t] = [c]
    
    answer = 1
    for items in closet.values():
        answer *= len(items) + 1
        
    return answer - 1