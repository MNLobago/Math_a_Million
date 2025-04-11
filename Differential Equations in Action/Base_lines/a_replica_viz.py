import matplotlib
import matplotlib.pyplot as plt
import numpy
import functools

def show_plot(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        plt.grid(True)
        plt.tight_layout()
        plt.show()
        return result
    return wrapper
