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


if __name__ == '__main__':
    unittest.main(verbosity=2)
