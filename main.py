import numpy as np
import matplotlib.pyplot as plt
from utils.data_generation import generate_points_from_function
from utils.interpolation import polynomial_interpolation
from utils.least_squares import polynomial_least_squares, trigonometric_least_squares

def plot_results(x, y, poly_interp, poly_least_squares, trig_least_squares, func=None):
    plt.scatter(x, y, color='black', label='Data Points')

    x_dense = np.linspace(min(x), max(x), 1000)
    plt.plot(x_dense, poly_interp(x_dense), label='Interpolation Polynomial', linestyle='--')
    plt.plot(x_dense, poly_least_squares(x_dense), label='Least Squares Polynomial', linestyle=':')
    plt.plot(x_dense, trig_least_squares(x_dense), label='Trigonometric Least Squares', linestyle='-.')

    if func is not None:
        plt.plot(x_dense, func(x_dense), label='Original Function', linestyle='-')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Approximation Techniques')
    plt.show()

def main():
    input_type = 'function'  

    if input_type == 'points':
        x = np.array([0, 1, 2, 3, 4, 5])
        y = np.array([1, 2, 1, 2, 1, 2])
    else:
        func = lambda x: 3 * x**3 - 2 * x + 5 * np.sin(x)
        interval = [0, 10]
        num_points = 20
        x, y = generate_points_from_function(func, interval, num_points)

    m = 5

    poly_interp = polynomial_interpolation(x, y)
    poly_least_squares = polynomial_least_squares(x, y, m)
    trig_least_squares = trigonometric_least_squares(x, y, m)

    plot_results(x, y, poly_interp, poly_least_squares, trig_least_squares, func if input_type == 'function' else None)

if __name__ == '__main__':
    main()
