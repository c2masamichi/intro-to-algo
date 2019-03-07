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


if __name__ == '__main__':
    unittest.main(verbosity=2)
