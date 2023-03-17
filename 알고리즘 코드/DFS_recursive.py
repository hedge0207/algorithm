def recursive_dfs(vertex, discovered=[]):
    discovered.append(vertex)
    for adjacent_vertex in graph[vertex]:
        if adjacent_vertex in discovered:
            continue
        else:
            recursive_dfs(adjacent_vertex, discovered)
    return discovered


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
print(recursive_dfs(start_vertex))
