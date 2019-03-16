import unittest

import prog
from prog import Node, Tree


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

    def test_iterative_tree_search(self):
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
                self.assertIs(prog.iterative_tree_search(x, k), expected)

    def test_tree_minimum(self):
        root = Node(6)
        root.left = Node(5, parent=root)
        root.right = Node(7, parent=root)
        expected = 5
        result = prog.tree_minimum(root)
        self.assertEqual(result.key, expected)

    def test_tree_maximum(self):
        root = Node(6)
        root.left = Node(5, parent=root)
        root.right = Node(7, parent=root)
        expected = 7
        result = prog.tree_maximum(root)
        self.assertEqual(result.key, expected)

    def test_tree_successor(self):
        root = Node(6)
        root.left = Node(5, parent=root)
        root.right = Node(7, parent=root)
        parameters = [
            (root, root.right),
            (root.left, root),
            (root.right, None),
        ]
        for x, expected in parameters:
            with self.subTest(x=x):
                self.assertIs(prog.tree_successor(x), expected)

    def test_tree_insert(self):
        root = Node(3)
        root.left = Node(1, parent=root)
        root.right = Node(5, parent=root)
        t = Tree(root)
        prog.tree_insert(t, Node(2))
        expected = [1, 2, 3, 5]
        result = []
        prog.inorder_tree_walk(t.root, result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
