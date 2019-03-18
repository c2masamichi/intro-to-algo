class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root


def inorder_tree_walk(x, result):
    if x is not None:
        inorder_tree_walk(x.left, result)
        result.append(x.key)
        inorder_tree_walk(x.right, result)


def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x is y.right:
        x = y
        y = y.parent
    return y


def tree_insert(t, z):
    y = None
    x = t.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def transplant(t, u, v):
    if u.parent is None:
        t.root = v
    elif u is u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent
