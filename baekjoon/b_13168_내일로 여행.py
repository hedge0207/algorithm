import sys

input = sys.stdin.readline
N, ticket_price = map(int, input().split())
cities = {city: i for i, city in enumerate(input().split())}
M = int(input())
vertices = input().split()
K = int(input())

MAX_COST = float("infinity")

graph = [[MAX_COST] * N for _ in range(N)]
discount_graph = [[MAX_COST] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
            discount_graph[i][j] = 0

discount_trains = ["S-Train", "V-Train"]
free_trains = ["ITX-Saemaeul", "ITX-Cheongchun", "Mugunghwa"]
for i in range(K):
    transport, start, end, cost = input().split()
    cost = int(cost)

    if transport in discount_trains:
        discount_cost = cost / 2
    elif transport in free_trains:
        discount_cost = 0.0
    else:
        discount_cost = cost

    if graph[cities[start]][cities[end]] > cost:
        graph[cities[start]][cities[end]] = cost
        graph[cities[end]][cities[start]] = cost
    if discount_graph[cities[start]][cities[end]] > discount_cost:
        discount_graph[cities[start]][cities[end]] = discount_cost
        discount_graph[cities[end]][cities[start]] = discount_cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            if discount_graph[i][j] > discount_graph[i][k] + discount_graph[k][j]:
                discount_graph[i][j] = discount_graph[i][k] + discount_graph[k][j]

discount_total = ticket_price
total = 0

start = cities[vertices[0]]
for vertex in vertices[1:]:
    end = cities[vertex]
    total += graph[start][end]
    discount_total += discount_graph[start][end]
    start = cities[vertex]

if discount_total >= total:
    print("No")
else:
    print("Yes")
