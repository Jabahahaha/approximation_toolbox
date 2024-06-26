import numpy as np
from scipy.optimize import curve_fit

def polynomial_least_squares(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    poly = np.poly1d(coeffs)
    return poly

def trigonometric_least_squares(x, y, m):
    def trig_func(x, *coeffs):
        c0 = coeffs[0]
        result = c0
        for i in range(1, m+1):
            result += coeffs[2*i-1] * np.sin(i * x) + coeffs[2*i] * np.cos(i * x)
        return result

    initial_guess = np.ones(2 * m + 1)
    coeffs, _ = curve_fit(trig_func, x, y, p0=initial_guess)
    return lambda x: trig_func(x, *coeffs)
