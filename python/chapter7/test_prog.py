import unittest

import prog


class TestClient(unittest.TestCase):

    def test_partition(self):
        parameters = [
            (
                ([4, 3, 1, 2], 0, 3),
                ([1, 2, 4, 3], 1)
            ),
            (
                ([2, 8, 7, 1, 3, 5, 6, 4], 0, 7),
                ([2, 1, 3, 4, 7, 5, 6, 8], 3),
            ),
        ]
        for args, expected in parameters:
            a, p, r = args
            after, q = expected
            with self.subTest(expected=expected):
                self.assertEqual(prog.partition(a, p, r), q)
                self.assertEqual(a, after)

    def test_quicksort(self):
        parameters = [
            (
                ([4, 3, 1, 3], 0, 3),
                [1, 3, 3, 4],
            ),
            (
                ([2, 8, 7, 1, 3, 5, 6, 4], 0, 7),
                [1, 2, 3, 4, 5, 6, 7, 8],
            ),
            (
                ([2, 4, 3, 1, 7, 6, 8, 5], 0, 3),
                [1, 2, 3, 4, 7, 6, 8, 5],
            ),
        ]
        for args, expected in parameters:
            a, p, r = args
            with self.subTest(expected=expected):
                prog.quicksort(a, p, r)
                self.assertEqual(a, expected)

    def test_randomized_partition(self):
        parameters = [
            (
                ([4, 3, 1, 2], 0, 3),
                (1, 2, 3, 4)
            ),
            (
                ([2, 8, 7, 1, 3, 5, 6, 4], 0, 7),
                (1, 2, 3, 4, 5, 6, 7, 8)
            ),
        ]
        for args, expected in parameters:
            a, p, r = args
            with self.subTest(expected=expected):
                self.assertIn(prog.partition(a, p, r), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
