import sys
input = sys.stdin.readline

def DFS(start):
    stack = [start]

    while stack:
        cur = stack.pop()

        for nxt in range(1, V + 1):
            if adj_matrix[cur][nxt] and nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)


V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1

visited = set()
ans = 0

for node in range(1, V + 1):
    if node not in visited:
        visited.add(node)
        DFS(node)
        ans += 1

print(ans)
