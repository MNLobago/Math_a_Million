# Deep Learning Activations

Welcome to the Deep Learning Activations folder! This folder contains Python scripts implementing various activation functions commonly used in deep learning neural networks.

## Contents

- [Sigmoid Activation](sigmoid.py): Implementation of the sigmoid activation function.
- [ReLU (Rectified Linear Unit) Activation](relu.py): Implementation of the ReLU activation function.
- [Tanh (Hyperbolic Tangent) Activation](tanh.py): Implementation of the tanh activation function.
- [Softmax Activation](softmax.py): Implementation of the softmax activation function.

Each script provides a simple implementation of the respective activation function along with brief explanations of their mathematical formulations and usage examples.

## Usage

To use any of the activation functions, simply import the corresponding Python module and call the function with your input data.

```python
import numpy as np
from sigmoid import sigmoid
from relu import relu
from tanh import tanh
from softmax import softmax

# Example usage
x = np.array([1.0, 2.0, 3.0])

# Sigmoid activation
print("Sigmoid of", x, ":", sigmoid(x))

# ReLU activation
print("ReLU of", x, ":", relu(x))

# Tanh activation
print("Tanh of", x, ":", tanh(x))

# Softmax activation
print("Softmax of", x, ":", softmax(x))
