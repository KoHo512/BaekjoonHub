def solution(l, r):
    answer = set()
    
    def add_05(num):
        if num > r:
            return
        
        if l <= num <= r:
            answer.add(num)
        
        add_05(num * 10)
        add_05(num * 10 + 5)
    
    add_05(5)
    
    return sorted(answer) if answer else [-1]