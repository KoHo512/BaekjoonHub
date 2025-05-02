from collections import deque

def solution(maps):
    
    def bfs(x, y):
        queue = deque([(x, y, 1)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx == n - 1 and ny == m - 1:
                    return distance + 1
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
                    
        return -1
                    
    n, m = len(maps), len(maps[0])
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    
    visited[x][y] = True
    return bfs(x, y)