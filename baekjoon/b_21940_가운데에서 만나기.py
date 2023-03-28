import sys

input = sys.stdin.readline
N, M = map(int, input().split())
MAX_COST = float("infinity")
graph = [[MAX_COST] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    st, ed, cost = map(int, input().split())
    graph[st][ed] = cost

num_friends = int(input())
cities = list(map(int, input().split()))

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_cost = float("infinity")
close_cities = []
for i in range(1, N + 1):
    max_ = -1
    for j in cities:
        if graph[i][j] == MAX_COST or graph[j][i] == MAX_COST:
            continue
        if graph[i][j] + graph[j][i] > max_:
            max_ = graph[i][j] + graph[j][i]
    if max_ == min_cost:
        close_cities.append(i)
    elif max_ < min_cost:
        min_cost = max_
        close_cities = [i]

for city in close_cities:
    print(city, end=" ")
