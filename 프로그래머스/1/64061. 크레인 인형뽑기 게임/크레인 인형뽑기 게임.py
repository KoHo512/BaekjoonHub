from collections import deque

def solution(board, moves):
    m, n = len(board[0]), len(board)
    
    queue = [deque() for _ in range(m)]
    basket = []
    answer = 0
    
    for x in range(m):
        for y in range(n-1, -1, -1):
            if board[y][x] > 0:
                queue[x].append(board[y][x])
    
    for move in moves:
        move -= 1
        if queue[move]:
            doll = queue[move].pop()

            if basket and basket[-1] == doll:
                answer += 2
                basket.pop()
            else:
                basket.append(doll)
    
    return answer 