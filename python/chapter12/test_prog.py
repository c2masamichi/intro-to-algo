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

    def test_tree_search(self):
        root = Node(6)
        root.left = Node(5, parent=root)
        root.right = Node(7, parent=root)
        parameters = [
            ((root, 6), root),
            ((root, 5), root.left),
            ((root, 7), root.right),
            ((root, 10), None),
        ]
        for args, expected in parameters:
            x, k = args
            with self.subTest(k=k):
                self.assertIs(prog.tree_search(x, k), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
