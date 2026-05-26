def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    answer = 1
    point = routes[0][1]
    
    for route in routes:
        if route[0] > point:
            answer += 1
            point = route[1]
    
    return answer