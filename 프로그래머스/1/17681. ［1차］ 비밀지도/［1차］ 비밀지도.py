def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a1 = arr1[i]
        a2 = arr2[i]
        
        line = ''
        for _ in range(n):
            if a1 % 2 or a2 % 2:
                line = '#' + line
            else:
                line = ' ' + line
            
            a1 //= 2
            a2 //= 2
                
        answer.append(line)
        
    return answer