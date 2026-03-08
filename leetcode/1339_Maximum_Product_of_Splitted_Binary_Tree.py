from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        sum_ = 0
        def _get_sum(node):
            nonlocal sum_
            sum_ += node.val
            if node.left:
                _get_sum(node.left)

            if node.right:
                _get_sum(node.right)
        _get_sum(root)

        ans = 0
        def dfs(node):
            nonlocal ans

            left = 0
            if node.left:
                left = dfs(node.left)
                ans = max(ans, (sum_ - left) * left)

            right = 0
            if node.right:
                right = dfs(node.right)
                ans = max(ans, (sum_ - right) * right)

            return left + right + node.val

        dfs(root)
        return ans % (10**9+7)