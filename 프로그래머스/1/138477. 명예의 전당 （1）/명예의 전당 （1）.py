def solution(k, score):
    answer = []
    honor = []
    
    for i in range(len(score)):
        if i < k:
            honor.append(score[i])
            answer.append(min(honor))
        else:
            if score[i] > min(honor):
                honor.append(score[i])
                honor.remove(min(honor))
            answer.append(min(honor))
        
    return answer