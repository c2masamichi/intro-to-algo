import unittest

import prog
from prog import Node, Tree


class TestClient(unittest.TestCase):

    def make_nodes(self, root_key, left_key=None, right_key=None):
        root = Node(root_key)
        if left_key is not None:
            root.left = Node(left_key, parent=root)
        if right_key is not None:
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
        parameters = (
            ((root, 6), root),
            ((root, 5), root.left),
            ((root, 7), root.right),
            ((root, 10), None),
        )
        for args, expected in parameters:
            x, k = args
            with self.subTest(k=k):
                self.assertIs(prog.tree_search(x, k), expected)

    def test_iterative_tree_search(self):
        root = self.make_nodes(6, 5, 7)
        parameters = (
            ((root, 6), root),
            ((root, 5), root.left),
            ((root, 7), root.right),
            ((root, 10), None),
        )
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
        parameters = (
            (root, root.right),
            (root.left, root),
            (root.right, None),
        )
        for x, expected in parameters:
            with self.subTest(x=x):
                self.assertIs(prog.tree_successor(x), expected)

    def test_tree_insert(self):
        parameters = (
            (
                (Tree(self.make_nodes(3, 1, 5)), Node(2)),
                [1, 2, 3, 5]
            ),
            (
                (Tree(self.make_nodes(3, 1, 5)), Node(6)),
                [1, 3, 5, 6]
            ),
            (
                (Tree(), Node(10)),
                [10]
            ),
        )
        for args, expected in parameters:
            t, z = args
            with self.subTest(expected=expected):
                prog.tree_insert(t, z)
                result = []
                prog.inorder_tree_walk(t.root, result)
                self.assertEqual(result, expected)

    def test_transplant(self):
        t1 = Tree(self.make_nodes(3, right_key=5))
        t2 = Tree(self.make_nodes(3, 1, 5))
        t3 = Tree(self.make_nodes(3, 1, 5))
        parameters = (
            (
                (t1, t1.root, t1.root.right),
                [5]
            ),
            (
                (t2, t2.root.left, t2.root.left.right),
                [3, 5]
            ),
            (
                (t3, t3.root.right, t3.root.right.right),
                [1, 3]
            ),
        )
        for args, expected in parameters:
            t, u, v = args
            with self.subTest(expected=expected):
                prog.transplant(t, u, v)
                result = []
                prog.inorder_tree_walk(t.root, result)
                self.assertEqual(result, expected)

    def test_tree_delete_simple(self):
        t1 = Tree(self.make_nodes(3, 1, 5))
        t2 = Tree(self.make_nodes(3, left_key=1))
        t3 = Tree(self.make_nodes(3, 1, 5))
        parameters = (
            (
                (t1, t1.root.left),
                [3, 5]
            ),
            (
                (t2, t2.root),
                [1]
            ),
            (
                (t3, t3.root),
                [1, 5]
            ),
        )
        for args, expected in parameters:
            t, z = args
            with self.subTest(expected=expected):
                prog.tree_delete(t, z)
                result = []
                prog.inorder_tree_walk(t.root, result)
                self.assertEqual(result, expected)

    def test_tree_delete_complex(self):
        t = Tree(self.make_nodes(5, 1, 9))
        t.root.right.left = self.make_nodes(7, right_key=8)
        t.root.right.left.parent = t.root.right
        t.root.right.right = Node(11, parent=t.root.right)
        expected = [1, 7, 8, 9, 11]
        prog.tree_delete(t, t.root)
        result = []
        prog.inorder_tree_walk(t.root, result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
