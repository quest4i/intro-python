import unittest
from holaxprogramming.algorithms import array


class TestArray(unittest.TestCase):
    """
    Tests that an exception occurs when the number of arguments is different.
    """

    def setUp(self):
        self.array = array.Array('1 2 3 4 10 11')

    def test_sum(self):
        result = self.array.sum(6)
        self.assertEqual(result, 31)



