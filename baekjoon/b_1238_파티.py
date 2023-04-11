from collections import defaultdict
import sys
import heapq


def dijkstra(st, graph):
    MAX_COST = float("inf")
    distance = [MAX_COST] * (N + 1)
    distance[st] = 0
    queue = [[0, st]]

    while queue:
        cost, vertex = heapq.heappop(queue)
        if distance[vertex] != cost:
            continue

        for additional_cost, neighbor in graph[vertex]:
            new_cost = cost + additional_cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(queue, [new_cost, neighbor])

    return distance


input = sys.stdin.readline
N, M, X = map(int, input().split())

start_to_dest = defaultdict(list)
dest_to_start = defaultdict(list)
for _ in range(M):
    st, ed, ct = map(int, input().split())
    start_to_dest[st].append([ct, ed])
    dest_to_start[ed].append([ct, st])

distance_from_start = dijkstra(X, start_to_dest)
distance_from_dest = dijkstra(X, dest_to_start)

result = -1
for cost_to_dest, cost_from_dest in zip(distance_from_start[1:], distance_from_dest[1:]):
    total_cost = cost_to_dest + cost_from_dest
    if total_cost > result:
        result = total_cost

print(result)