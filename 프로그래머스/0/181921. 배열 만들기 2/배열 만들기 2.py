def solution(l, r):
    answer = set()
    
    def add_05(num):
        if l <= num <= r:
            answer.add(num)
            
        if num > r:
            return
        
        add_05(int(str(num)+"5"))
        add_05(int(str(num)+"0"))
    
    add_05(5)
    
    return sorted(answer) if answer else [-1]