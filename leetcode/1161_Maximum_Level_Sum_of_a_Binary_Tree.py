from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_per_level = defaultdict(int)
        def dfs(node, level):
            sum_per_level[level] += node.val
            if node.left is not None:
                dfs(node.left, level + 1)

            if node.right is not None:
                dfs(node.right, level + 1)
        dfs(root, 1)

        ans = 0
        max_ = 0
        for level, sum_ in sum_per_level.items():
            if sum_ < max_:
                max_ = sum_
                ans = level
        return ans