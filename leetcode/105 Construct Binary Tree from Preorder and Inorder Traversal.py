from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            val = preorder.pop(0)
            parent_index = inorder.index(val)

            tree = TreeNode(val)
            tree.left = self.buildTree(preorder, inorder[:parent_index])
            tree.right = self.buildTree(preorder, inorder[parent_index+1:])
            return tree