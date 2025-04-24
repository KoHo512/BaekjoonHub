def solution(places):
    answer = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check_distance(place):
        place = [list(line) for line in place]
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[nx][ny] == "P" or place[nx][ny] == "Z":
                                return 0
                            
                            if place[nx][ny] == "O":
                                place[nx][ny] = "Z"
                                continue
        return 1
            
    return [check_distance(place) for place in places]