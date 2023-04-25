from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return node, 0

            right, rcnt = dfs(node.right)
            left, lcnt = dfs(node.left)

            if right and node.val == right.val:
                rcnt += 1
            else:
                rcnt = 0

            if left and node.val == left.val:
                lcnt += 1
            else:
                lcnt = 0

            sum_ = rcnt + lcnt
            if sum_ > self.result:
                self.result = sum_

            return node, max(rcnt, lcnt)

        dfs(root)

        return self.result
