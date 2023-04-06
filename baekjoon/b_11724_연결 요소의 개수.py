from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v):
    for neighbor in graph[v]:
        if visited[neighbor]:
            continue
        visited[neighbor] = 1
        dfs(neighbor)


input = sys.stdin.readline
N, M = map(int, input().split())
visited = [0] * (N + 1)
graph = defaultdict(list)

for _ in range(M):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

cnt = 0
for vertex in list(graph):
    if visited[vertex]:
        continue
    cnt += 1
    visited[vertex] = 1
    dfs(vertex)
print(cnt + visited.count(0) - 1)