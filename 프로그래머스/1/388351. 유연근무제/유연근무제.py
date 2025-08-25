def solution(schedules, timelogs, startday):
    answer = 0
    
    for time, logs in zip(schedules, timelogs):
        day = startday - 1
        
        if time % 100 + 10 >= 60:
            checktime = (time // 100 + 1) * 100 + (time % 100 - 50)
        else:
            checktime = time + 10
        
        for log in logs:
            day += 1
            if day > 7: day = 1
            
            if day == 6 or day == 7:
                continue
                
            if checktime < log:
                break
        else:
            answer += 1
            
    return answer