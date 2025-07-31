def solution(mats, park):
    m, n = len(park[0]), len(park)
    mats = sorted(mats, reverse=True)
    
    def check_mat(i, j, mat):
        for a in range(i, i + mat):
            for b in range(j, j + mat):
                if a >= n or b >= m:
                    return False
                if park[a][b] != "-1":
                    return False
        return True
        
    for mat in mats:
        for i in range(n):
            for j in range(m):
                if park[i][j] == "-1":
                    if check_mat(i, j, mat):
                        return mat
    
    return -1
            