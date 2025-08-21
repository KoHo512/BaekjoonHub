import math

def solution(progresses, speeds):
    answer = []
    max_day, total = 0, 1
    
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)

        if day <= max_day:
            total += 1
        else:
            if max_day != 0:
                answer.append(total)
            max_day = day
            total = 1
    
    answer.append(total)
    
    return answer