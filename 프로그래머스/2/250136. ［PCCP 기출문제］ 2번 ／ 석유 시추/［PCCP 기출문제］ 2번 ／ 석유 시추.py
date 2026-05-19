from collections import deque

def solution(land):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    n, m = len(land), len(land[0])
    
    group = 2
    groups = {}
    
    def bfs(sr, sc, g):
        queue = deque([(sr, sc)])
        land[sr][sc] = g
        count = 1
        
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1:
                    land[nr][nc] = g
                    count += 1
                    queue.append((nr, nc))
        
        return count
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                groups[group] = bfs(i, j, group)
                group += 1
                
    answer = [0] * m
    
    for j in range(m):
        total = set()
        for i in range(n):
            if land[i][j] > 1:
                total.add(land[i][j])
        answer[j] = sum([groups[t] for t in total])
        
    return max(answer)