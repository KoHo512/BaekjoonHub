def solution(park, routes):
    h, w = len(park), len(park[0])
    
    def start_at():
        for x in range(h):
            for y in range(w):
                if park[x][y] == "S":
                    return x, y
                
    x, y = start_at()
    
    for route in routes:
        d, n = route.split()
        n = int(n)
        
        if d == "N":
            nx, ny = x - n, y
            s = -1
        elif d == "S":
            nx, ny = x + n, y
            s = 1
        elif d == "W":
            nx, ny = x, y - n
            s = -1
        else:
            nx, ny = x, y + n
            s = 1
            
        if not (0 <= nx < h and 0 <= ny < w):
            continue
        
        if d in ["N", "S"]:
            for i in range(x, nx + s, s):
                if park[i][ny] == "X":
                    break
            else:
                x, y = nx, ny
        else:
            for j in range(y, ny + s, s):
                if park[nx][j] == "X":
                    break
            else:
                x, y = nx, ny
            
    return [x, y]