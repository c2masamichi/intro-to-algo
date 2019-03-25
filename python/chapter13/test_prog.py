import unittest

import prog
from prog import Node, Tree, BLACK, RED


class TestClient(unittest.TestCase):

    def make_nodes(self, root_key, left_key=None, right_key=None):
        root = Node(root_key)
        if left_key is not None:
            root.left = Node(left_key, parent=root)
        if right_key is not None:
            root.right = Node(right_key, parent=root)
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
        y.left = Node(y_left_key, parent=y)
        y.right = Node(y_right_key, parent=y)
        prog.left_rotate(t, x)
        parameters = [
            (t.root.key, y_key),
            (t.root.left.key, x_key),
            (t.root.left.left.key, x_left_key),
            (t.root.left.right.key, y_left_key),
            (t.root.right.key, y_right_key),
        ]
        for key, expected in parameters:
            with self.subTest(expected=expected):
                self.assertEqual(key, expected)

    def test_right_rotate(self):
        y_key = 7
        y_right_key = 11
        x_key = 3
        x_left_key = 1
        x_right_key = 5
        t = Tree(self.make_nodes(y_key, x_key, y_right_key))
        y = t.root
        x = t.root.left
        x.left = Node(x_left_key, parent=x)
        x.right = Node(x_right_key, parent=x)
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
