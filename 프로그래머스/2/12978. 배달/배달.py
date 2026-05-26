def solution(N, road, K):
    answer = [float("INF")] * N
    
    graph = [[float("INF")] * N for _ in range(N)]
    for n1, n2, k in road:
        graph[n1 - 1][n2 - 1] = min(graph[n1 - 1][n2 - 1], k)
        graph[n2 - 1][n1 - 1] = min(graph[n2 - 1][n1 - 1], k)

    def dfs(n):
        for i in range(N):
            if i != n and graph[n][i] != float("INF"):
                if answer[i] >= answer[n] + graph[n][i]:
                    answer[i] = answer[n] + graph[n][i]
                    dfs(i)
    
    answer[0] = 0
    dfs(0)
    
    return len([a for a in answer if a <= K])