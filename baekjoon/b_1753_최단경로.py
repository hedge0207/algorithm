from collections import defaultdict
import heapq
import sys


input = sys.stdin.readline

N, M = map(int, input().split())
MAX_COST = float("infinity")
distances = [MAX_COST] * (N + 1)
START_VERTEX = int(input())
distances[START_VERTEX] = 0

graph = defaultdict(list)

for _ in range(M):
    frm, to, cost = map(int, input().split())
    graph[frm].append([cost, to])

queue = [(0, START_VERTEX)]

while queue:
    cur_dist, cur = heapq.heappop(queue)
    if distances[cur] != cur_dist:
        continue

    for new_dist, neighbor in graph[cur]:
        new_dist = cur_dist + new_dist
        if new_dist < distances[neighbor]:
            distances[neighbor] = new_dist
            heapq.heappush(queue, (new_dist, neighbor))

for i in distances[1:]:
    if i < MAX_COST:
        print(i)
    else:
        print("INF")