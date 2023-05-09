from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def postorder_traversal(node):
            if node is None:
                return

            postorder_traversal(node.left)
            postorder_traversal(node.right)
            if low <= node.val <= high:
                self.result += node.val

        postorder_traversal(root)
        return self.result

    # best practice
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def postorder_traversal(node):
            if node is None:
                return 0

            if node.val < low:
                return postorder_traversal(node.right)
            elif node.val > high:
                return postorder_traversal(node.left)
            else:
                return node.val + postorder_traversal(node.right) + postorder_traversal(node.left)

        return postorder_traversal(root)
