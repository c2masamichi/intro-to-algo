class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def inorder_tree_walk(x, result):
    if x is not None:
        inorder_tree_walk(x.left, result)
        result.append(x.key)
        inorder_tree_walk(x.right, result)
