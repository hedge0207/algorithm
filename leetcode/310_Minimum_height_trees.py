from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for st, ed in edges:
            tree[st].append(ed)
            tree[ed].append(st)

        leaves = [node for node in tree if len(tree[node]) == 1] or [0]

        while n > 2:
            n -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                parent = tree[leaf].pop()
                tree[parent].remove(leaf)

                if len(tree[parent]) == 1:
                    next_leaves.append(parent)

            leaves = next_leaves

        return leaves