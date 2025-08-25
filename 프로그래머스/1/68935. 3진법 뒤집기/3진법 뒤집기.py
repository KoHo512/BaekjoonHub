def solution(n):
    n3 = []
    
    while n:
        n3.append(n % 3)
        n //= 3
        
    return int(''.join(map(str, n3)), 3)