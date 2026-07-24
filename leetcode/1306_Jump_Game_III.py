from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        graph = {}
        for i in range(len(arr)):
            reachable_nodes = []
            if i + arr[i] < len(arr):
                reachable_nodes.append(i+arr[i])
            if i - arr[i] >= 0:
                reachable_nodes.append(i-arr[i])
            graph[i] = reachable_nodes

        queue = deque(graph[start])
        visited = [0] * len(arr)
        visited[start] = 1
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = 1
                queue.append(neighbor)
        return False