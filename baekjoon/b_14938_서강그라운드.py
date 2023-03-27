import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())
num_items = list(map(int, input().split()))

MAX_COST = float("infinity")
graph = [[MAX_COST] * (N + 1) for _ in range(N + 1)]

for _ in range(R):
    st, ed, cost = map(int, input().split())
    graph[st][ed] = cost
    graph[ed][st] = cost

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_num_item = -1
for i in range(1, N + 1):
    num_item = 0
    for j in range(1, N + 1):
        if graph[i][j] <= M:
            num_item += num_items[j-1]
    if num_item > max_num_item:
        max_num_item = num_item

print(max_num_item)