def solution(n):
    answer = []
    
    # while n > 0:
    #     answer.append(n % 10)
    #     n //= 10
    
    answer = [int(i) for i in str(n)[::-1]]
        
    return answer