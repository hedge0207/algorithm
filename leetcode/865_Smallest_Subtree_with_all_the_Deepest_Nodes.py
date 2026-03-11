from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_depth = 0
        depth_per_node = defaultdict(int)

        common_node = set()
        def dfs(node: Optional[TreeNode], depth: int, path: set):
            nonlocal deepest_depth, common_node, depth_per_node

            if node is None:
                if depth > deepest_depth:
                    common_node = path
                    deepest_depth = depth
                elif depth == deepest_depth:
                    common_node = common_node.intersection(path)
                return

            depth_per_node[node.val] = depth
            path.add(node)
            dfs(node.left, depth+1, path)
            dfs(node.right, depth+1 ,path)
            path.remove(node)

        dfs(root, 0, set())
        ans = root
        max_depth = 0
        for node in common_node:
            if depth_per_node[node.val] > max_depth:
                ans = node
                max_depth = depth_per_node[node.val]
        return ans


# best_practice
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]