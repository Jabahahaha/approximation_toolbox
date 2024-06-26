import unittest
import numpy as np
from utils.data_generation import generate_points_from_function

class TestDataGeneration(unittest.TestCase):
    def test_generate_points_from_function(self):
        func = lambda x: x**2
        interval = [0, 10]
        num_points = 5
        x, y = generate_points_from_function(func, interval, num_points)
        expected_x = np.array([0, 2.5, 5, 7.5, 10])
        expected_y = np.array([0, 6.25, 25, 56.25, 100])
        np.testing.assert_array_almost_equal(x, expected_x)
        np.testing.assert_array_almost_equal(y, expected_y)

if __name__ == '__main__':
    unittest.main()
