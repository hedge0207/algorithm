from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        serialized_tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node:
                val = node.val
            else:
                val = None
            serialized_tree.append(str(val))
            if val is None:
                continue
            queue.append(node.left)
            queue.append(node.right)

        return ' '.join(serialized_tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split()
        root_val = nodes[0]
        if root_val == "None":
            return
        root = TreeNode(int(root_val))
        queue = deque([root])
        idx = 0
        while queue:
            node = queue.popleft()
            idx += 1
            if nodes[idx] != "None":
                left_node = TreeNode(int(nodes[idx]))
                node.left = left_node
                queue.append(left_node)

            idx += 1
            if nodes[idx] != "None":
                right_node = TreeNode(int(nodes[idx]))
                node.right = right_node
                queue.append(right_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))