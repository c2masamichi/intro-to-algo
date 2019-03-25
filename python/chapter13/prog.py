BLACK = 0
RED = 1


class Node:
    def __init__(self, key, color=BLACK, parent=None, left=None, right=None):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root


def left_rotate(t, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        t.root = y
    elif x is x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def right_rotate(t, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        t.root = x
    elif y is y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x
