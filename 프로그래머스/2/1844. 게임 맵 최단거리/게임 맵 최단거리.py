def solution(maps):
    # answer = 0
    
    M = len(maps)
    N = len(maps[0])
    
    visit = [[-1 for _ in range(N)] for _ in range(M)]
    
    q = []
    q.append([0, 0])
    visit[0][0] = 1
    
    while q:
        row, col = q.pop(0)
        
        # if row == N - 1 and col == M - 1:
        #     return answer
        
        if col + 1 < N and visit[row][col + 1] == -1 and maps[row][col + 1] == 1:
            visit[row][col + 1] = visit[row][col] + 1
            q.append([row, col + 1])
        if col - 1 >= 0 and visit[row][col - 1] == -1 and maps[row][col - 1] == 1:
            visit[row][col - 1] = visit[row][col] + 1
            q.append([row, col - 1])
        if row + 1 < M and visit[row + 1][col] == -1 and maps[row + 1][col] == 1:
            visit[row + 1][col] = visit[row][col] + 1
            q.append([row + 1, col])
        if row - 1 >= 0 and visit[row - 1][col] == -1 and maps[row - 1][col] == 1:
            visit[row - 1][col] = visit[row][col] + 1
            q.append([row - 1, col])

    return visit[M - 1][N - 1]