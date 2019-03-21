BLACK = 0
RED = 1


class Node:
    def __init__(self, color, key=None, parent=None, left=None, right=None):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.nil = Node(BLACK)
