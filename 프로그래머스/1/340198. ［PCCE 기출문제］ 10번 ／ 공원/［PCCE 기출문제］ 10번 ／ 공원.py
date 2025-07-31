def solution(mats, park):
    m, n = len(park[0]), len(park)
    mats.sort(reverse=True)
    
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i -1][j - 1]) + 1
            
    max_value = max(max(line) for line in dp)
    
    for mat in mats:
        if mat <= max_value:
            return mat
        
    return -1