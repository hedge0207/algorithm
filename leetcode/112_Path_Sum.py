from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    target_sum = 0

    def has_path(self, node, sum_):
        if node.left is None and node.right is None:
            if sum_ + node.val == self.target_sum:
                return True

        if node.left:
            ans = self.has_path(node.left, sum_ + node.val)
            if ans:
                return ans

        if node.right:
            ans = self.has_path(node.right, sum_ + node.val)
            if ans:
                return ans

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            self.target_sum = targetSum
            return self.has_path(root, 0)
        return False


# best practice
# https://leetcode.com/problems/path-sum/solutions/3977919/easy-solution-python3-c-c-c-java-explain-line-by-line-with-image
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum
