from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        def form_bst(l, r):
            if l >= r:
                return None
            m = (l + r) // 2
            node = nodes[m]
            node.left = form_bst(l, m)
            node.right = form_bst(m + 1, r)
            return node

        return form_bst(0, len(nodes))