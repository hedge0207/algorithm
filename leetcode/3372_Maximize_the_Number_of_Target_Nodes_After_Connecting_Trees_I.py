from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        tree1 = defaultdict(list)
        n = 2
        for edge in edges1:
            tree1[edge[0]].append(edge[1])
            tree1[edge[1]].append(edge[0])
            n = max(n, edge[0]+1, edge[1]+1)

        tree2 = defaultdict(list)
        m = 2
        for edge in edges2:
            tree2[edge[0]].append(edge[1])
            tree2[edge[1]].append(edge[0])
            m = max(m, edge[0]+1, edge[1]+1)

        max_val = 1
        for i in range(m):
            queue = [i]
            visited = [0] * m
            visited[i] = 1
            dist = 0
            num_connected_nodes_per_dist = [0] * k
            while queue and k > dist:
                num_connected_nodes_per_dist[dist] = len(queue)
                if dist > 0:
                    num_connected_nodes_per_dist[dist] += num_connected_nodes_per_dist[dist - 1]
                max_val = max(max_val, num_connected_nodes_per_dist[dist])
                new_queue = []
                for node in queue:
                    for neighbor in tree2[node]:
                        if visited[neighbor] == 1:
                            continue
                        new_queue.append(neighbor)
                        visited[neighbor] = 1
                queue = new_queue
                dist += 1

        ans = []
        for i in range(n):
            queue = [i]
            visited = [0] * n
            visited[i] = 1
            dist = 0
            num_connected_nodes_per_dist = [0] * (k+1)
            while queue and k >= dist:
                new_queue = []
                num_connected_nodes_per_dist[dist] = len(queue)
                if dist > 0:
                    num_connected_nodes_per_dist[dist] += num_connected_nodes_per_dist[dist - 1]
                for node in queue:
                    for neighbor in tree1[node]:
                        if visited[neighbor] == 1:
                            continue
                        new_queue.append(neighbor)
                        visited[neighbor] = 1
                queue = new_queue
                dist += 1
            num = max(num_connected_nodes_per_dist)
            if k > 0:
                num += max_val
            ans.append(num)

        return ans