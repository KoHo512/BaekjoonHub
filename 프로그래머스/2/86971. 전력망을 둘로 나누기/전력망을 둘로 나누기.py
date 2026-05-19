def solution(n, wires):
    answer = n
    
    tree = [[] for _ in range(n)]  
    for w1, w2 in wires:
        tree[w1 - 1].append(w2 - 1)
        tree[w2 - 1].append(w1 - 1)
        
    visited = [False] * n
    def dfs(cur):
        nonlocal answer
        visited[cur] = True
        count = 1
        
        for nxt in tree[cur]:
            if not visited[nxt]:
                count += dfs(nxt)
        
        answer = min(answer, abs(n - 2 * count))
        return count
        
    dfs(0)
    
    return answer