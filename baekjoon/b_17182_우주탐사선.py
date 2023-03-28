import sys


def recur(k, d, sum_cost):
    global result

    if sum_cost > result:
        return

    if d == N - 1:
        result = min(result, sum_cost)
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            recur(i, d + 1, sum_cost + graph[k][i])
            visit[i] = 0


input = sys.stdin.readline
N, K = map(int, input().split())
MAX_COST = float("infinity")
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

visit = [0] * N
visit[K] = 1
result = MAX_COST
recur(K, 0, 0)
print(result)
