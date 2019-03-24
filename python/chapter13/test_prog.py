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
        self.assertEqual(t.root.key, y_key)
        self.assertEqual(t.root.left.key, x_key)
        self.assertEqual(t.root.left.left.key, x_left_key)
        self.assertEqual(t.root.left.right.key, y_left_key)
        self.assertEqual(t.root.right.key, y_right_key)


if __name__ == '__main__':
    unittest.main(verbosity=2)
