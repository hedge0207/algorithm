import sys


input = sys.stdin.readline
N = int(input())
M = int(input())
MAX_COST = float("infinity")
graph = [[MAX_COST] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    st, ed, cost = map(int, input().split())
    graph[st][ed] = min(cost, graph[st][ed])

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            if graph[s][t] > graph[s][k] + graph[k][t]:
                graph[s][t] = graph[s][k] + graph[k][t]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == float("infinity"):
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()
