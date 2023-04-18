from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, depth, root):
        if root is None:
            if depth > self.max_depth:
                self.max_depth = depth
            return

        self.dfs(depth + 1, root.left)
        self.dfs(depth + 1, root.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(0, root)
        return self.max_depth
