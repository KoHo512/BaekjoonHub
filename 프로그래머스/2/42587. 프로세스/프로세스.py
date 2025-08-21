from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    
    while queue:
        process = queue.popleft()
        location -= 1
        
        if not queue:
            return answer + 1
        
        if process < max(queue):
            queue.append(process)
            if location == -1:
                location = len(queue) - 1
        else:
            answer += 1

        if location == -1:
            return answer