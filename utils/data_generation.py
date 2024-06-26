import numpy as np

def generate_points_from_function(func, interval, num_points):
    x_vals = np.linspace(interval[0], interval[1], num_points)
    y_vals = np.array([func(x) for x in x_vals])
    return x_vals, y_vals
