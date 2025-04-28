import sys

input = sys.stdin.readline

com_num = int(input())
line_num = int(input())

graph = [[] for _ in range(com_num + 1)]

for _ in range(line_num):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (com_num + 1)

def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

visited[1] = True
dfs(1)

print(sum(visited) - 1)