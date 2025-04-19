from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = -1

        def dfs(d, node):
            if node is None:
                return -1
            right = dfs(d + 1, node.right) + 1
            left = dfs(d + 1, node.left) + 1
            sum_ = right + left
            if sum_ > self.result:
                self.result = sum_
            return max(right, left)

        dfs(0, root)
        return self.result