def solution(d, budget):
    total = 0
    d.sort()
    
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            return i
    
    return len(d)