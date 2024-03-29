"""
N, M
start_vertex
st, ed, cost
6 8
1
1 2 3
1 3 2
1 4 5
2 3 2
2 5 8
3 4 2
4 5 6
5 6 1
"""

from collections import defaultdict
import heapq
import sys


input = sys.stdin.readline

N, M = map(int, input().split())
MAX_COST = float("infinity")
distances = [MAX_COST] * (N + 1)
START_VERTEX = int(input())
distances[START_VERTEX] = 0
pre = [0] * (N + 1)

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
            pre[neighbor] = cur
            heapq.heappush(queue, (new_dist, neighbor))

print(distances[1:])
print(pre[1:])
