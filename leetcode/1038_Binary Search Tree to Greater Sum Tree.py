class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum_ = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if node is None:
                return

            inorder_traversal(node.right)
            self.sum_ += node.val
            node.val = self.sum_
            inorder_traversal(node.left)

        inorder_traversal(root)
        return root