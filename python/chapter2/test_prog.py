import unittest

import prog


class TestClient(unittest.TestCase):

    def test_insertion_sort(self):
        parameters = [
            ([3], [3]),
            ([3, 4, 1, 2], [1, 2, 3, 4]),
            ([2, 5, 4, 1, 3, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
        ]
        for a, expected in parameters:
            with self.subTest(a=a):
                prog.insertion_sort(a)
                self.assertEqual(a, expected)

    def test_merge(self):
        parameters = [
            (
               ([3, 4, 1, 2], 0, 1, 3),
               [1, 2, 3, 4]
            ),
            (
               ([5, 8, 6, 7, 3, 4, 1, 2], 0, 1, 3),
               [5, 6, 7, 8, 3, 4, 1, 2]
            ),
            (
               ([5, 8, 6, 7, 3, 4, 1, 2], 4, 5, 7),
               [5, 8, 6, 7, 1, 2, 3, 4]
            ),
        ]
        for args, expected in parameters:
            a, p, q, r = args
            with self.subTest(args=args):
                prog.merge(a, p, q, r),
                self.assertEqual(a, expected)

    def test_merge_sort(self):
        parameters = [
            ([3], [3]),
            ([4, 3, 1, 2], [1, 2, 3, 4]),
            ([2, 5, 4, 1, 3, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
        ]
        for a, expected in parameters:
            with self.subTest(a=a):
                prog.merge_sort(a, 0, len(a) - 1)
                self.assertEqual(a, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
