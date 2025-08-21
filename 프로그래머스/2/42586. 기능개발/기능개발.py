import math

def solution(progresses, speeds):
    days = []
    
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100 - progress) / speed))
    
    answer = []
    max_day, total = 0, 1
    
    for day in days:
        if day <= max_day:
            total += 1
        else:
            if max_day != 0:
                answer.append(total)
            max_day = day
            total = 1
    
    answer.append(total)
    
    return answer