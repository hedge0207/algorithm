from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = root
        max_depth = -1
        def dfs(node, depth):
            nonlocal result, max_depth
            if node is None:
                return -1

            left_max_depth = dfs(node.left, depth + 1)
            right_max_depth = dfs(node.right, depth + 1)

            if left_max_depth == right_max_depth == -1:
                if max_depth < depth:
                    max_depth = depth
                    result = node
                return depth
            else:
                if left_max_depth == right_max_depth:
                    if max_depth <= left_max_depth:
                        max_depth = left_max_depth
                        result = node
                    return left_max_depth
                else:
                    greater_depth = left_max_depth
                    if right_max_depth > left_max_depth:
                        greater_depth = right_max_depth
                    return greater_depth

        dfs(root, 0)
        return result
