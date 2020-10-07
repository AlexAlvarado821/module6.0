import unittest
from more_functions import string_functions as str_funct

class MyTestCase(unittest.TestCase):
    def test_multiple_strings(self):
        self.assertEqual("AyahAyahAyah", str_funct.multiply_string("Ayah", 3))




if __name__ == '__main__':
    unittest.main()
