def solution(n):
    answer = 0
    n3 = []
    
    while n:
        n3.append(n % 3)
        n //= 3
        
    for i, num in enumerate(n3[::-1]):
        answer += num * 3**i
        
    return answer
        
        