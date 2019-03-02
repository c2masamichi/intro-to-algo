import unittest

import prog


class TestClient(unittest.TestCase):

    def test_sort_by_priority(self):
        parameters = [
            (
                ([10], [1]),
                [10]
            ),
            (
                ([10, 20, 30], [2, 3, 1]),
                [30, 10, 20]
            ),
        ]
        for args, expected in parameters:
            a, p = args
            with self.subTest(args=args):
                prog.sort_by_priority(a, p),
                self.assertEqual(a, expected)

    def test_permute_by_sorting(self):
        parameters = [
            [3],
            [3, 2, 5, 1],
            [10, 2, 2, 4, 4, 3, 7],
        ]
        for a in parameters:
            with self.subTest(a=a):
                expected = a[:]
                prog.permute_by_sorting(a)
                self.assertCountEqual(a, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
