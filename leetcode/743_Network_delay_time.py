from collections import defaultdict
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        for st, ed, cost in times:
            graph[st].append([cost, ed])

        queue = [[0, k]]

        while queue:
            cost, vertex = heapq.heappop(queue)

            if distances[vertex] != cost:
                continue

            for additional_cost, neighbor in graph[vertex]:
                new_cost = distances[vertex] + additional_cost
                if distances[neighbor] > new_cost:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, [new_cost, neighbor])

        if (max_value := max(distances[1:])) < float("inf"):
            return max_value

        return -1


s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
