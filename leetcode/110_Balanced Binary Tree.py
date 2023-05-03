from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursive_func(node):
            if node is None:
                return 0

            left = recursive_func(node.left)
            right = recursive_func(node.right)

            if abs(left - right) <= 1 and left != -1 and right != -1:
                return max(left, right) + 1
            else:
                return -1

        return recursive_func(root) != -1