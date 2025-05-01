def solution(numbers, target):
    
    def dfs(depth, total):
        # 1. 종료 조건
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return
        
        # 2. 정화식(재귀식)
        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])
        
    answer = 0
    dfs(1, numbers[0])
    dfs(1, -numbers[0])
    
    return answer