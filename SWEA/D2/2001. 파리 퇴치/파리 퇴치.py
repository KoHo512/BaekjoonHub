T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]
    maxFlies = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            killedFlies = 0
            for i in range(M):
                for j in range(M):
                    killedFlies += flies[r + i][c + j]
            maxFlies = max(killedFlies, maxFlies)

    print(f"#{tc} {maxFlies}")
