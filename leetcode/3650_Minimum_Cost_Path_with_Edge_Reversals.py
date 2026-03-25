from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for s, d, w in edges:
            graph[s].append([d, w])
            graph[d].append([s, w * 2])
        distance = [float("inf")] * n
        distance[0] = 0
        queue = [[0, 0]]

        def dijkstra():
            while queue:
                cur_dist, cur = heapq.heappop(queue)
                if distance[cur] != cur_dist:
                    continue

                for neighbor, weight in graph[cur]:
                    new_dist = cur_dist + weight
                    if new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor))

        dijkstra()
        ans = distance[-1]
        if isinstance(ans, float):
            return -1
        else:
            return ans