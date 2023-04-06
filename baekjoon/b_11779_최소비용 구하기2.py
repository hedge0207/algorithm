from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
MAX_COST = float("inf")
distance = [MAX_COST] * (N + 1)
pre = [0] * (N + 1)
graph = defaultdict(list)
for _ in range(M):
    st, ed, cost = map(int, input().split())
    graph[st].append([cost, ed])
START, END = map(int, input().split())
distance[START] = 0

queue = [[0, START]]

while queue:
    cost, vertex = heapq.heappop(queue)
    if distance[vertex] != cost:
        continue

    for additinal_cost, dest in graph[vertex]:
        new_cost = distance[vertex] + additinal_cost
        if distance[dest] > new_cost:
            distance[dest] = new_cost
            pre[dest] = vertex
            heapq.heappush(queue, [new_cost, dest])

print(distance[END])
v = END
path = []
while True:
    path.append(v)
    if pre[v] == START:
        path.append(START)
        break
    v = pre[v]

print(len(path))
for i in path[::-1]:
    print(i, end=" ")
