import unittest

import prog
from prog import Node


class TestClient(unittest.TestCase):

    def test_inorder_tree_walk(self):
        root = Node(6)
        root.left = Node(5, parent=root)
        root.right = Node(7, parent=root)
        expected = [5, 6, 7]
        result = []
        prog.inorder_tree_walk(root, result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
