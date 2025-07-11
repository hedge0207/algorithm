from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
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
        queue = [0]
        visited = [0] * m
        visited[0] = 1
        dist = 1
        num_connected_nodes_per_dist = [0] * (m+1)
        while queue:
            num_connected_nodes_per_dist[dist] = len(queue)
            if dist % 2 == 0:
                if dist >= 3:
                    num_connected_nodes_per_dist[dist] += num_connected_nodes_per_dist[dist - 2]
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
        max_val = max(max_val, m-max_val)

        dist_from_root_node = [0]*n
        ans = []
        queue = [0]
        visited = [0] * n
        visited[0] = 1
        dist = 0
        num_connected_nodes_per_dist = [0] * n
        val = 1
        while queue:
            new_queue = []
            num_connected_nodes_per_dist[dist] = len(queue)
            if dist % 2 == 0:
                if dist >= 2:
                    num_connected_nodes_per_dist[dist] += num_connected_nodes_per_dist[dist - 2]
                val = max(val, num_connected_nodes_per_dist[dist])
            for node in queue:
                dist_from_root_node[node] = dist
                for neighbor in tree1[node]:
                    if visited[neighbor] == 1:
                        continue
                    new_queue.append(neighbor)
                    visited[neighbor] = 1
            queue = new_queue
            dist += 1

        for dist in dist_from_root_node:
            if dist % 2 == 0:
                ans.append(val + max_val)
            else:
                ans.append(n-val + max_val)

        return ans






















s = Solution()
print(s.maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))
print(s.maxTargetNodes([[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]]))
print(s.maxTargetNodes([[0,1]], [[0,1]]))
print(s.maxTargetNodes([[0,1]], [[0,1],[1,2]]))
print(s.maxTargetNodes([[5,1],[7,2],[6,4],[0,6],[8,0],[3,8],[5,3],[7,5],[7,9]], [[3,0],[8,2],[5,3],[1,4],[5,6],[1,7],[5,1],[5,8]]))

"""
[8, 7, 7, 8, 8]
[3, 6, 6, 6, 6]
[2, 2]
[3, 3]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
"""