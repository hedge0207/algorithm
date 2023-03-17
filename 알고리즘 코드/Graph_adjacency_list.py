v, e = 6, 7

edges = [
    [1, 2], [1, 5], [2, 3], [2, 5],
    [3, 4], [4, 5], [4, 6]
]

# 유향 그래프
graph = {i: [] for i in range(1, v + 1)}
for edge in edges:
    graph[edge[0]].append(edge[1])

for vertex, adjecency_vertexes in graph.items():
    print(vertex, adjecency_vertexes)

print("-"*100)
# 무향 그래프
graph = {i: [] for i in range(1, v + 1)}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for vertex, adjecency_vertexes in graph.items():
    print(vertex, adjecency_vertexes)