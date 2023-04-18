# 전위 순회
def preorder_traversal(root):
    if root == 0:
        return
    visited.append(root)
    preorder_traversal(lc[root])
    preorder_traversal(rc[root])

# 중위 순회
def inorder_traversal(root):
    if root == 0:
        return
    inorder_traversal(lc[root])
    visited.append(root)
    inorder_traversal(rc[root])

def postorder_traversal(root):
    if root == 0:
        return
    postorder_traversal(lc[root])
    postorder_traversal(rc[root])
    visited.append(root)

lc = [0, 2, 4, 6, 0, 0, 0, 0, 0]
rc = [0, 3, 5, 7, 0, 8, 0, 0, 0]
visited = []
preorder_traversal(1)
print(visited)			# [1, 2, 4, 5, 8, 3, 6, 7]
visited = []
inorder_traversal(1)
print(visited)          # [4, 2, 5, 8, 1, 6, 3, 7]
visited = []
postorder_traversal(1)
print(visited)          # [4, 8, 5, 2, 6, 7, 3, 1]