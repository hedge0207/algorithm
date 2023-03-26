import sys


input = sys.stdin.readline
N = int(input())
M = int(input())
MAX_COST = float("infinity")
graph = [[MAX_COST] * (N + 1) for _ in range(N + 1)]
nxt = [[MAX_COST] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    st, ed, cost = map(int, input().split())

    if cost < graph[st][ed]:
        graph[st][ed] = cost
        nxt[st][ed] = ed

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            if graph[s][t] > graph[s][k] + graph[k][t]:
                graph[s][t] = graph[s][k] + graph[k][t]
                nxt[s][t] = nxt[s][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        path = [i]
        start = i
        while 1:
            vertex = nxt[start][j]
            if vertex == MAX_COST:
                break
            path.append(vertex)
            start = vertex

        if len(path) == 1:
            print(0)
        else:
            print("{}에서 {}로 가는 최단 경로:".format(i, j), end=" ")
            for v in path:
                print(v, end=" ")
            print()
