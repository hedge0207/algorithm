from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        MAX_COST = float("inf")
        distances = [MAX_COST] * n
        distances[src] = 0

        for s, d, c in flights:
            graph[s].append([c, d])

        queue = [[0, src, 0]]

        while queue:
            cnt, vertex, cost = heapq.heappop(queue)
            if cnt > k:
                continue

            for additional, neighbor in graph[vertex]:
                new_cost = cost + additional
                if distances[neighbor] > new_cost:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, [cnt+1, neighbor, new_cost])

        if (ans := distances[dst]) < MAX_COST:
            return ans
        else:
            return -1