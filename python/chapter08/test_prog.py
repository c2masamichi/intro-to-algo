import unittest

import prog


class TestClient(unittest.TestCase):

    def test_counting_sort(self):
        parameters = (
            (
                ([3, 0, 1, 2], [0] * 4, 3),
                [0, 1, 2, 3]
            ),
            (
                ([2, 5, 3, 0, 2, 3, 0, 3], [0] * 8, 5),
                [0, 0, 2, 2, 3, 3, 3, 5]
            ),
        )
        for args, expected in parameters:
            a, b, k = args
            with self.subTest(expected=expected):
                prog.counting_sort(a, b, k)
                self.assertEqual(b, expected)

    def test_counting_sort_by_digit(self):
        parameters = (
            (
                ([53, 90, 91, 12], 1),
                [90, 91, 12, 53]
            ),
            (
                ([90, 91, 12, 53], 2),
                [12, 53, 90, 91]
            ),
            (
                ([534, 504, 415, 193, 612, 652, 302, 787, 482], 2),
                [504, 302, 415, 612, 534, 652, 787, 482, 193]
            ),
        )
        for args, expected in parameters:
            a, d = args
            with self.subTest(expected=expected):
                self.assertEqual(
                    prog.counting_sort_by_digit(a, d), expected)

    def test_radix_sort(self):
        parameters = (
            (
                ([3, 0, 7, 9, 1], 1),
                [0, 1, 3, 7, 9]
            ),
            (
                ([90, 91, 12, 53], 2),
                [12, 53, 90, 91]
            ),
            (
                ([534, 504, 415, 193, 612, 652, 302, 787, 482], 3),
                [193, 302, 415, 482, 504, 534, 612, 652, 787]
            ),
        )
        for args, expected in parameters:
            a, d = args
            with self.subTest(expected=expected):
                self.assertEqual(
                    prog.radix_sort(a, d), expected)

    def test_insertion_sort(self):
        parameters = (
            ([3], [3]),
            ([3, 4, 1, 2], [1, 2, 3, 4]),
            ([2, 5, 4, 1, 3, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
        )
        for a, expected in parameters:
            with self.subTest(expected=expected):
                prog.insertion_sort(a)
                self.assertEqual(a, expected)

    def test_bucket_sort(self):
        parameters = (
            ([0.1], [0.1]),
            ([0.3, 0.4, 0.1, 0.2], [0.1, 0.2, 0.3, 0.4]),
            (
                [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
                [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
            ),
        )
        for a, expected in parameters:
            with self.subTest(expected=expected):
                self.assertEqual(prog.bucket_sort(a), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
