import unittest
import numpy as np
from utils.least_squares import polynomial_least_squares, trigonometric_least_squares

class TestLeastSquares(unittest.TestCase):
    def test_polynomial_least_squares(self):
        x = np.array([0, 1, 2])
        y = np.array([1, 2, 0])
        degree = 2
        poly = polynomial_least_squares(x, y, degree)
        np.testing.assert_almost_equal(poly(1), 2)

    def test_trigonometric_least_squares(self):
        x = np.array([0, np.pi/2, np.pi])
        y = np.array([0, 1, 0])
        m = 1
        trig_approx = trigonometric_least_squares(x, y, m)
        np.testing.assert_almost_equal(trig_approx(np.pi/2), 1, decimal=1)

if __name__ == '__main__':
    unittest.main()
