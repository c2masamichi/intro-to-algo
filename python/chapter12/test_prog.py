import unittest

import prog
from prog import Node, Tree


class TestClient(unittest.TestCase):

    def make_nodes(self, root_key, left_key, right_key):
        root = Node(root_key)
        root.left = Node(left_key, parent=root)
        root.right = Node(right_key, parent=root)
        return root

    def test_inorder_tree_walk(self):
        root = self.make_nodes(6, 5, 7)
        expected = [5, 6, 7]
        result = []
        prog.inorder_tree_walk(root, result)
        self.assertEqual(result, expected)

    def test_tree_search(self):
        root = self.make_nodes(6, 5, 7)
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
        root = self.make_nodes(6, 5, 7)
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
        root = self.make_nodes(6, 5, 7)
        expected = 5
        result = prog.tree_minimum(root)
        self.assertEqual(result.key, expected)

    def test_tree_maximum(self):
        root = self.make_nodes(6, 5, 7)
        expected = 7
        result = prog.tree_maximum(root)
        self.assertEqual(result.key, expected)

    def test_tree_successor(self):
        root = self.make_nodes(6, 5, 7)
        parameters = [
            (root, root.right),
            (root.left, root),
            (root.right, None),
        ]
        for x, expected in parameters:
            with self.subTest(x=x):
                self.assertIs(prog.tree_successor(x), expected)

    def test_tree_insert(self):
        t = Tree(self.make_nodes(3, 1, 5))
        prog.tree_insert(t, Node(2))
        expected = [1, 2, 3, 5]
        result = []
        prog.inorder_tree_walk(t.root, result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
