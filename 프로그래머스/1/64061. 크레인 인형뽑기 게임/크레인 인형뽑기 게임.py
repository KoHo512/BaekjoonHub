def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move -= 1
        
        for line in board:
            if line[move] > 0:
                if basket and basket[-1] == line[move]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(line[move])
                
                line[move] = 0
                break            
            
    return answer