import sys

input = sys.stdin.readline

def dfs(node):
    if not tree[node]:
        return 1

    leafs = 0

    for next_node in tree[node]:
        leafs += dfs(next_node)

    return leafs

n = int(input())
parents = list(map(int, input().split()))
target = int(input())

tree = [[] for _ in range(n)]

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
        continue

    if parent == target or child == target:
        continue

    tree[parent].append(child)

if target == root:
    print(0)
else:
    print(dfs(root))