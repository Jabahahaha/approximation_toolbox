import unittest
import numpy as np
from utils.interpolation import polynomial_interpolation

class TestInterpolation(unittest.TestCase):
    def test_polynomial_interpolation(self):
        x = np.array([0, 1, 2])
        y = np.array([1, 2, 0])
        poly = polynomial_interpolation(x, y)
        np.testing.assert_almost_equal(poly(1), 2)

if __name__ == '__main__':
    unittest.main()
