def solution(park, routes):
    h, w = len(park), len(park[0])
    
    def find_s():
        for i in range(h):
            for j in range(w):
                if park[i][j] == "S":
                    return i, j
                
    x, y = find_s()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    direction = {"N": 0, "S": 1, "W": 2, "E": 3}
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        d = direction.get(op)
        
        nx, ny = x, y
        for i in range(n):
            nx, ny = nx + dx[d], ny + dy[d]
            
            if 0 <= nx < h and 0 <= ny < w:
                if park[nx][ny] == "X":
                    break
            else:
                break        
        else:
            x, y = nx, ny
            
    return [x, y]