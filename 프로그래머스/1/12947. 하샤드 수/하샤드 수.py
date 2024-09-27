def solution(x):
    sum_digit = 0
    y = x
    
    for _ in range(len(str(x))):
        sum_digit += y % 10
        y //= 10
        
    if x % sum_digit == 0:
        return True
        
    return False