import unittest
from utils import calculate_bmi, calculate_bmr

class TestUtils(unittest.TestCase):
    
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        
    def test_calculate_bmr_male(self):
        self.assertAlmostEqual(calculate_bmr(170, 70, 23, 'male'), 1711.41, places=2)
        
    def test_calculate_bmr_female(self):
        self.assertAlmostEqual(calculate_bmr(160, 70, 23, 'female'), 1490.97, places=2)

if __name__ == '__main__':
    unittest.main()
