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


if __name__ == '__main__':
    unittest.main(verbosity=2)
