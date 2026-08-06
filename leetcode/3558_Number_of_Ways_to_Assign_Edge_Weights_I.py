from collections import defaultdict


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        tree = defaultdict(list)
        for s, e in edges:
            if s < e:
                tree[s].append(e)
            else:
                tree[e].append(s)

        height = 0
        def find_height(node, d):
            nonlocal height

            height = max(height, d)

            for child in tree[node]:
                find_height(child, d+1)

        find_height(1, 0)

        return (2**(height-1)) % (10**9 + 7)