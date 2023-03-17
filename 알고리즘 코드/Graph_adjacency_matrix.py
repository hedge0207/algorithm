v, e = 6, 7

edges = [
    [1, 2], [1, 5], [2, 3], [2, 5],
    [3, 4], [4, 5], [4, 6]
]

# 무향 그래프의 구현
graph = [[0] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    vertex, another_vertex = edges[i]
    graph[vertex][another_vertex] = 1
    graph[another_vertex][vertex] = 1

for i in range(e):
    print(graph[i])

print("-"*100)
# 유향 그래프 구현
graph = [[0] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    vertex, another_vertex = edges[i]
    graph[vertex][another_vertex] = 1

for i in range(e):
    print(graph[i])