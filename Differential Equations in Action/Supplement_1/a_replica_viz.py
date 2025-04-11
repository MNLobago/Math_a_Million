import matplotlib.pyplot as plt
import functools

# A decorator to automatically display the plot after the function runs
def show_plot(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

        # Customize plot colors (assumes first line is sin, second is cos)
        lines = plt.gca().get_lines()
        if len(lines) >= 2:
            lines[0].set_color('red')    # sin(x)
            lines[1].set_color('green')  # cos(x)

        plt.xlabel("x (radians)")
        plt.ylabel("Values")
        plt.title("Sine and Cosine Waves")
        plt.legend(["sin(x)", "cos(x)"])
        plt.grid(True)
        plt.show()
    return wrapper
