def solution(s):
    answer = []
    alpha = {}
    
    for i in range(len(s)):
        if s[i] in alpha.keys():
            answer.append(i - alpha[s[i]])
            alpha[s[i]] = i
        else:
            answer.append(-1)
            alpha[s[i]] = i
            
    return answer