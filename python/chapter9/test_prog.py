import unittest

import prog


class TestClient(unittest.TestCase):

    def test_minimum(self):
        parameters = [
            ([3], 3),
            ([3, 10, -4, 2, -5, 0, 7], -5),
        ]
        for a, expected in parameters:
            with self.subTest(expected=expected):
                self.assertEqual(prog.minimum(a), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
