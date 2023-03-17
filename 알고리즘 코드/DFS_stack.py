graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

start_vertex = 1
stack = [start_vertex]
discovered = []
while stack:
    vertex = stack.pop()
    if vertex not in discovered:
        discovered.append(vertex)
        for adjacent_vertex in graph[vertex]:
            stack.append(adjacent_vertex)

print(discovered)



