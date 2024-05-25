import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid function for the input x.

    Args:
    x (float or numpy.ndarray): Input value or array.

    Returns:
    float or numpy.ndarray: Sigmoid of the input value or array.
    """
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    # Example usage
    x = 0
    print("Sigmoid of", x, ":", sigmoid(x))

    x_array = np.array([-1, 0, 1])
    print("Sigmoid of", x_array, ":", sigmoid(x_array))