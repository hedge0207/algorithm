from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_depth = float("inf")

    def _dfs(self, k, node):
        if node.left is None and node.right is None:
            self.min_depth = min(self.min_depth, k)
            return

        if node.left is not None:
            self._dfs(k + 1, node.left)

        if node.right is not None:
            self._dfs(k + 1, node.right)

    def _bfs(self, root):
        queue = [root]
        depth = 1
        while queue:
            new_queue = []

            for node in queue:
                is_leaf = True
                if node.left:
                    new_queue.append(node.left)
                    is_leaf = False

                if node.right:
                    new_queue.append(node.right)
                    is_leaf = False

                if is_leaf:
                    return depth

            depth += 1
            queue = new_queue

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            # self._dfs(1, root)
            # return self.min_depth
            return self._bfs(root)
        else:
            return 0
