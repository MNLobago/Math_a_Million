import numpy as np

def relu(x):
    """
    Compute the ReLU (Rectified Linear Unit) function for the input x.

    Args:
    x (float or numpy.ndarray): Input value or array.

    Returns:
    float or numpy.ndarray: ReLU of the input value or array.
    """
    return np.maximum(0, x)

if __name__ == "__main__":
    # Example usage
    x = 0
    print("ReLU of", x, ":", relu(x))

    x_array = np.array([-1, 0, 1])
    print("ReLU of", x_array, ":", relu(x_array))
