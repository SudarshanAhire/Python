import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    pass 

# Neuron calculation 
def Marvellous_neuron_forward(inputs, weights, bias):
    # 1) Display inputs and weights 
    print("Inputs (x):", inputs)
    print("Weights (w):", weights)
    print("Bias (b):", bias)

    # 2) Summation z = wx + b 
    z = sum(w*x for w, x in zip(inputs, weights)) + bias
    print("Summation (z = wx + b):", z)

    # 3) Activation function output 
    y_hat = sigmoid(z)
    print("Activation Function Sigmoid")
    print("Output (y_hat = sigmoid(z)):", y_hat)

    return z, y_hat


def plot_sigmoid():
    pass

def main():
    # Example inputs, weights, and bias 
    inputs = [1.0, 2.0, 3.0]       # Example input features
    weights = [0.6, 0.4, -0.2]     # Weights for each input

    bias = 0.5       # Bias term

    # Run the neuron forward pass 
    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)

    # Plot sigmoid curve
    plot_sigmoid()


if __name__ == "__main__":
    main()