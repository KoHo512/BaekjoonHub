from collections import deque

def solution(priorities, location):
    queue = deque([(i, prior) for i, prior in enumerate(priorities)])
    answer = 0
    
    while queue:
        i, process = queue.popleft()
        
        if not queue:
            return answer + 1
        
        if process < max([prior for _, prior in queue]):
            queue.append((i, process))
        else:
            answer += 1
            
            if i == location:
                return answer