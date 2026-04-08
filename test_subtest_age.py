import unittest
from age import categorize_by_age

class TestCategorizeByAgeSubtest(unittest.TestCase):

    def test_is_child(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")

    def test_is_adult(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")

    def test_is_golden(self):
        for age in range(66, 101):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")

if __name__ == '__main__':
    unittest.main(verbosity=2)