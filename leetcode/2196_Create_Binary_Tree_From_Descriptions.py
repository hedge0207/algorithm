from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        child_per_parent = defaultdict(list)
        children = set()
        for p, c, is_left in descriptions:
            child_per_parent[p].append([c, is_left])
            children.add(c)

        root = None
        for parent in child_per_parent.keys():
            if parent not in children:
                root = TreeNode(parent)
                break

        def _make_binary_tree(node: TreeNode):
            children = child_per_parent[node.val]
            for c, is_left in children:
                child_node = TreeNode(c)
                if is_left:
                    node.left = child_node
                else:
                    node.right = child_node
                _make_binary_tree(child_node)

        _make_binary_tree(root)
        return root



# best practice
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes={}
        children=set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent]=TreeNode(parent)
            if child not in nodes:
                nodes[child]=TreeNode(child)
            if is_left:
                nodes[parent].left=nodes[child]
            else:
                nodes[parent].right=nodes[child]
            children.add(child)

        for val in nodes:
            if val not in children:
                return nodes[val]