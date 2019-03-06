import unittest

import prog


class TestClient(unittest.TestCase):

    def test_parent(self):
        parameters = [
            (4, 2),
            (5, 2),
        ]
        for v, expected in parameters:
            with self.subTest(v=v):
                self.assertEqual(prog.parent(v), expected)

    def test_left(self):
        parameters = [
            (1, 2),
            (2, 4),
        ]
        for v, expected in parameters:
            with self.subTest(v=v):
                self.assertEqual(prog.left(v), expected)

    def test_right(self):
        parameters = [
            (1, 3),
            (2, 5),
        ]
        for v, expected in parameters:
            with self.subTest(v=v):
                self.assertEqual(prog.right(v), expected)

    def test_max_heapify(self):
            parameters = [
                (
                    ([-1, 3, 4, 5, 2, 1], 1),
                    [-1, 5, 4, 3, 2, 1]
                ),
                (
                    ([-1, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 2),
                    [-1, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
                ),
            ]
            for args, expected in parameters:
                a, i = args
                with self.subTest(args=args):
                    prog.max_heapify(a, i),
                    self.assertEqual(a, expected)

    def test_build_max_heap(self):
            parameters = [
                (
                    [-1, 1, 2, 3],
                    [-1, 3, 2, 1]
                ),
                (
                    [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
                    [-1, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
                ),
            ]
            for a, expected in parameters:
                with self.subTest(a=a):
                    prog.build_max_heap(a),
                    self.assertEqual(a, expected)

    def test_heapsort(self):
            parameters = [
                (
                    [-1, 2, 3, 2, 1],
                    [-1, 1, 2, 2, 3]
                ),
                (
                    [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
                    [-1, 1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
                ),
                (
                    [100, 2, 3, 1],
                    [100, 1, 2, 3]
                ),
            ]
            for a, expected in parameters:
                with self.subTest(a=a):
                    prog.heapsort(a),
                    self.assertEqual(a, expected)

    def test_heap_maximum(self):
        a = [-1, 3, 2, 1]
        self.assertEqual(prog.heap_maximum(a), 3)

    def test_heap_extract_max(self):
            parameters = [
                (
                    [-1, 4, 2, 3, 1],
                    (4, [-1, 3, 2, 1])
                ),
                (
                    [-1, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1],
                    (16, [-1, 14, 8, 10, 4, 7, 9, 3, 2, 1])
                ),
            ]
            for a, expected in parameters:
                maxv, after = expected
                with self.subTest(a=a):
                    self.assertEqual(prog.heap_extract_max(a), maxv)
                    self.assertEqual(a, after)

            with self.assertRaises(Exception) as e:
                prog.heap_extract_max([-1])
            self.assertEqual(e.exception.args[0], 'Heap Underflow')

    def test_heap_increase_key(self):
            parameters = [
                (
                    ([-1, 3, 2, 1], 2, 4),
                    [-1, 4, 3, 1]
                ),
                (
                    ([-1, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 9, 15),
                    [-1, 16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
                ),
            ]
            for args, expected in parameters:
                a, i, key = args
                with self.subTest(args=args):
                    prog.heap_increase_key(a, i, key),
                    self.assertEqual(a, expected)

    def test_max_heap_insert(self):
            parameters = [
                (
                    ([-1, 4, 3, 2], 1),
                    [-1, 4, 3, 2, 1]
                ),
                (
                    ([-1, 4, 3, 2], 5),
                    [-1, 5, 4, 2, 3]
                ),
                (
                    ([-1, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 15),
                    [-1, 16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7]
                ),
            ]
            for args, expected in parameters:
                a, key = args
                with self.subTest(args=args):
                    prog.max_heap_insert(a, key),
                    self.assertEqual(a, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
