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


"""
input
순서대로 vertex의 개수 N
간선의 개수 M
3번째 줄 부터 M+2번 줄까지 출발 정점, 도착 정점, 가중치

5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""


# 경로 복원
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
