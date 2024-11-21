from collections import deque

V = int(input())
E = int(input())

adj_lst = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)


queue = deque([1])
visited = set([1])

while queue:
    cur = queue.popleft()

    for nxt in adj_lst[cur]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)

ans = len(visited) - 1
print(ans)
