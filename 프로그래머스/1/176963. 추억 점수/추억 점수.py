def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        total = 0
        for n in p:
            if n in name:
                total += yearning[name.index(n)]
        answer.append(total)
                
    return answer