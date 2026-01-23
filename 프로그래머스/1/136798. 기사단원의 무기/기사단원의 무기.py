def solution(number, limit, power):
    answer = 0
    
    for n in range(1, number + 1):
        total = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                total += 2
                
                if i * i == n:
                    total -= 1
                
        if total <= limit:
            answer += total
        else:
            answer += power
        
    return answer