import numpy as np

def tanh(x):
    """
    Compute the hyperbolic tangent (tanh) function for the input x.

    Args:
    x (float or numpy.ndarray): Input value or array.

    Returns:
    float or numpy.ndarray: tanh of the input value or array.
    """
    return np.tanh(x)

if __name__ == "__main__":
    # Example usage
    x = 0
    print("tanh of", x, ":", tanh(x))

    x_array = np.array([-1, 0, 1])
    print("tanh of", x_array, ":", tanh(x_array))
