from collections import deque

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    bmaps = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        bmaps[i][1 : m + 1] = maps[i - 1]
        
    queue = deque([(1, 1, 1)])
    bmaps[1][1] = 0
    ans = -1
    
    while queue:
        r, c, cnt = queue.popleft()
        
        if r == n and c == m:
            ans = cnt
            break
            
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if bmaps[nr][nc]:
                bmaps[nr][nc] = 0
                queue.append((nr, nc, cnt + 1))
        
    return ans
    