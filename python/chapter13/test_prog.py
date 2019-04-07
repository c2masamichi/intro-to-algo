import unittest

import prog
from prog import Node, Tree, BLACK, RED


class TestClient(unittest.TestCase):

    def add_children(self, root, left_key=None, right_key=None):
        if left_key is not None:
            root.left = Node(left_key, parent=root)
        if right_key is not None:
            root.right = Node(right_key, parent=root)

    def make_nodes(self, root_key, left_key=None, right_key=None):
        root = Node(root_key)
        self.add_children(root, left_key, right_key)
        return root

    def test_left_rotate(self):
        x_key = 5
        x_left_key = 1
        y_key = 9
        y_left_key = 7
        y_right_key = 11
        t = Tree(self.make_nodes(x_key, x_left_key, y_key))
        x = t.root
        y = t.root.right
        self.add_children(y, y_left_key, y_right_key)
        prog.left_rotate(t, x)
        parameters = [
            (t.root, y_key),
            (t.root.right, y_right_key),
            (t.root.left, x_key),
            (t.root.left.left, x_left_key),
            (t.root.left.right, y_left_key),
        ]
        for n, expected in parameters:
            with self.subTest(expected=expected):
                self.assertEqual(n.key, expected)

    def test_right_rotate(self):
        y_key = 7
        y_right_key = 11
        x_key = 3
        x_left_key = 1
        x_right_key = 5
        t = Tree(self.make_nodes(y_key, x_key, y_right_key))
        y = t.root
        x = t.root.left
        self.add_children(x, x_left_key, x_right_key)
        prog.right_rotate(t, y)
        parameters = [
            (t.root, x_key),
            (t.root.left, x_left_key),
            (t.root.right, y_key),
            (t.root.right.left, x_right_key),
            (t.root.right.right, y_right_key),
        ]
        for n, expected in parameters:
            with self.subTest(expected=expected):
                self.assertEqual(n.key, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
