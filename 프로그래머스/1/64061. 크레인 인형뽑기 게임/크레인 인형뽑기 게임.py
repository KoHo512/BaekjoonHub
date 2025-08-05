from collections import deque

def solution(board, moves):
    m, n = len(board[0]), len(board)
    
    queue = [deque() for _ in range(m)]
    basket = deque()
    answer = 0
    
    for x in range(m):
        for y in range(n-1, -1, -1):
            if board[y][x] > 0:
                queue[x].append(board[y][x])
    
    for move in moves:
        if queue[move - 1]:
            basket.append(queue[move - 1].pop())
        
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                answer += 2
                basket.pop()
                basket.pop()
    
    return answer