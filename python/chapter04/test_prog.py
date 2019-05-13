import unittest

import prog


class TestClient(unittest.TestCase):

    def test_find_max_crossing_subarray(self):
        parameters = (
            (
                ([1, 2, 3, 4, 5], 0, 2, 4),
                (0, 4, 15)
            ),
            (
                ([10, -1, -1, -1, -1, -1, -1, 10], 1, 3, 6),
                (3, 4, -2)
            ),
            (
                ([-2, 3, -2, 3, 4, 2, -5, -1], 0, 3, 7),
                (1, 5, 10)
            ),
        )
        for args, expected in parameters:
            a, low, mid, high = args
            with self.subTest(args=args):
                self.assertEqual(
                    prog.find_max_crossing_subarray(a, low, mid, high),
                    expected
                )

    def test_find_maximum_subarray(self):
        parameters = (
            (
                ([5], 0, 0),
                (0, 0, 5)
            ),
            (
                ([10, 11, 21], 1, 1),
                (1, 1, 11)
            ),
            (
                ([2, 2, 2, 2, 2], 0, 4),
                (0, 4, 10)
            ),
            (
                ([-2, -3, -1, -2, -5], 0, 4),
                (2, 2, -1)
            ),
            (
                ([-2, -2, -2, -2, -2], 0, 4),
                (0, 0, -2)
            ),
            (
                ([10, -5, -6, 5, 6, -2, -3, 2], 0, 7),
                (3, 4, 11)
            ),
        )
        for args, expected in parameters:
            a, low, high = args
            with self.subTest(args=args):
                self.assertEqual(
                    prog.find_maximum_subarray(a, low, high),
                    expected
                )

    def test_square_matrix_multiply(self):
        parameters = (
            (
                [
                    [1, 2],
                    [3, 4]
                ],
                [
                    [1, 0],
                    [0, 1]
                ],
                [
                    [1, 2],
                    [3, 4]
                ]
            ),
            (
                [
                    [1, 2],
                    [3, 4]
                ],
                [
                    [2, 1],
                    [1, 2]
                ],
                [
                    [4, 5],
                    [10, 11]
                ]
            ),
        )
        for a, b, expected in parameters:
            with self.subTest(a=a, b=b):
                self.assertEqual(
                    prog.square_matrix_multiply(a, b),
                    expected
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
