from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_distance = 10 ** 5
    prev = -(10 ** 5)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def traval_tree(node):
            if node.left:
                traval_tree(node.left)

            if node.val - self.prev < self.min_distance:
                self.min_distance = node.val - self.prev
            self.prev = node.val

            if node.right:
                traval_tree(node.right)

        traval_tree(root)

        return self.min_distance
