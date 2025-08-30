from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    maps[0][0] = -1
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, nums = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx == n - 1 and ny == m - 1:
                return nums + 1
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = -1
                queue.append((nx, ny, nums + 1))
    
    return -1