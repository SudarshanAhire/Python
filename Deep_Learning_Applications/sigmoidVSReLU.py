import math 
import matplotlib.pyplot as plt 
import numpy as np 

#-------------------------
# Activation Functions
#-------------------------

def sigmoid(z):
    # sigmoid function : squashes values to (0, 1).
    return 1 / (1 + math.exp(-z))

def ReLU(z):
    # ReLU function : outputs z if positive, else 0.
    return max(0, z)

#-------------------------
# Neuron calculation 
#-------------------------

def Marvellous_neuron_forward(inputs, weights, bias, activation_func):
    # 1) Display the inputs and weights 
    print("Inputs (x):", inputs)
    print("Weights (w):", weights)
    print("Bias (b):", bias)

    # 2) Summation 
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w.x + b):", z)

    # 3) Activation 
    y_hat = activation_func(z)
    print(f"Activation Function : {activation_func.__name__}")
    print(f"Output (y_hat): {y_hat}\n")

    return z, y_hat

#-------------------------
# Plot sigmoid and ReLU
#-------------------------

def plot_sigmoid_relu():
    
    z_values = np.linspace(-10, 10, 200)
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)

    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2, color="blue")
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2, color="green")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.title("Sigmoid vs ReLU Activation Function", fontsize=16)
    plt.xlabel("Summation (z):", fontsize=14)
    plt.ylabel("Activation Output :", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

def main():
    # Example inputs, weights, bias 
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    print("=== Sigmoid Neuron ===")
    Marvellous_neuron_forward(inputs, weights, bias, sigmoid)

    print("=== ReLU Neuron ===")
    Marvellous_neuron_forward(inputs, weights, bias, ReLU)

    # Plot comaparision 
    plot_sigmoid_relu()

if __name__ == "__main__":
    main()