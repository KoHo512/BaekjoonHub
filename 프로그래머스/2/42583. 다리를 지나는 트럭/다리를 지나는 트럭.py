from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    trucks = deque(truck_weights)
    
    time = 0
    total = 0
    
    while trucks:
        time += 1
        truck = trucks.popleft()
        
        if len(bridge) == bridge_length: 
            total -= bridge.popleft()
        
        if total + truck <= weight:
            total += truck
            bridge.append(truck)
        else:
            bridge.append(0)
            trucks.appendleft(truck)
        
    return time + bridge_length