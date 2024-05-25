import numpy as np

def softmax(x):
    """
    Compute the softmax function for the input x.

    Args:
    x (numpy.ndarray): Input array.

    Returns:
    numpy.ndarray: Softmax of the input array.
    """
    exp_x = np.exp(x - np.max(x))  # Subtract max(x) for numerical stability
    return exp_x / np.sum(exp_x)

if __name__ == "__main__":
    # Example usage
    x = np.array([1.0, 2.0, 3.0])
    print("Softmax of", x, ":", softmax(x))
