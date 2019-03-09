import unittest

import prog


class TestClient(unittest.TestCase):

    def test_counting_sort(self):
        parameters = [
            (
                ([3, 0, 1, 2], [0] * 4, 3),
                [0, 1, 2, 3]
            ),
            (
                ([2, 5, 3, 0, 2, 3, 0, 3], [0] * 8, 5),
                [0, 0, 2, 2, 3, 3, 3, 5]
            ),
        ]
        for args, expected in parameters:
            a, b, k = args
            with self.subTest(expected=expected):
                prog.counting_sort(a, b, k)
                self.assertEqual(b, expected)

    def test_counting_sort_by_digit(self):
        parameters = [
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
        ]
        for args, expected in parameters:
            a, d = args
            with self.subTest(expected=expected):
                self.assertEqual(
                    prog.counting_sort_by_digit(a, d), expected)

    def test_radix_sort(self):
        parameters = [
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
        ]
        for args, expected in parameters:
            a, d = args
            with self.subTest(expected=expected):
                self.assertEqual(
                    prog.radix_sort(a, d), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
