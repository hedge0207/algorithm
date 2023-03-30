import sys


input = sys.stdin.readline
N, M = map(int, input().split())
MAX_COST = float("infinity")
graph = [[MAX_COST] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    st, ed, b = map(int, input().split())

    if b == 1:
        graph[st][ed] = 0
        graph[ed][st] = 0
    else:
        graph[st][ed] = 0
        graph[ed][st] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


K = int(input())
for _ in range(K):
    st, ed = map(int, input().split())
    print(graph[st][ed])
