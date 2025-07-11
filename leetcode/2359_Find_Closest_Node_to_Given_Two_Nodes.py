class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def dfs(d, node, dist_from_node):
            if dist_from_node[node] < d:
                return

            if node == -1:
                return

            dist_from_node[node] = d
            dfs(d+1, edges[node], dist_from_node)

        dist_from_node1 = [float("inf")] * len(edges)
        dfs(0, node1, dist_from_node1)
        dist_from_node2 = [float("inf")] * len(edges)
        dfs(0, node2, dist_from_node2)

        min_dist = float("inf")
        ans = -1
        for i in range(len(edges)):

            if dist_from_node1[i] == float("inf") or dist_from_node2[i] == float("inf"):
                continue

            max_dist = max(dist_from_node1[i], dist_from_node2[i])
            if min_dist > max_dist:
                min_dist = max_dist
                ans = i

        return ans





























s = Solution()
print(s.closestMeetingNode([2,2,3,-1],0,1))
print(s.closestMeetingNode([1,2,-1],0,2))