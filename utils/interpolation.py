from scipy.interpolate import lagrange

def polynomial_interpolation(x, y):
    poly = lagrange(x, y)
    return poly
