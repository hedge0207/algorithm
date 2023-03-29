import sys


input = sys.stdin.readline
V, E = map(int, input().split())
MAX_COST = float("infinity")
graph = [[MAX_COST] * (V + 1) for _ in range(V + 1)]
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(E):
    st, ed, cost = map(int, input().split())
    graph[st][ed] = cost

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = MAX_COST
for i in range(V+1):
    for j in range(V+1):
        if i == j:
            continue
        result = min(result, graph[i][j] + graph[j][i])

for i in graph:
    print(i)

if result == MAX_COST:
    print(-1)
else:
    print(result)
