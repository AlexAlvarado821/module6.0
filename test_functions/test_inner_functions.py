import unittest

from more_functions import inner_functions_assignment as inner

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(inner.measures([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(inner.measures([3.5]), "Perimeter = 14.0 Area = 12.25")
    def test_measurements_no_measurements(self):
        with self.assertRaises(IndexError):
            inner.measures([])
    def test_measurements_too_many_measurements(self):
        with self.assertRaises(IndexError):
            inner.measures([2.4, 3.1, 3.6, 5.0])

if __name__ == '__main__':
    unittest.main()
