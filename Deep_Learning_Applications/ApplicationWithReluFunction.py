# ---------------------------------------------------
# Program : Artificial Neuron with ReLU Activation 
# Author : Sudarshan Gokul Ahire 
# ---------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------
# Step 1 - Activation Function (ReLU)
# ---------------------------------------------------
# ReLU = max(0, z)
# if z is positive -> output z 
# if z is negative -> output 0 

def relu(z):
    return max(0, z)

# ---------------------------------------------------
# Step 2 - Neuron Forward Pass Function
# ---------------------------------------------------
# This function simulates a single artificial neuron 
# It performs: 
# 1. Input * Weight multiplication 
# 2. Summation + Bias 
# 3. Activation (ReLU)

def Marvellous_neuron_forward(inputs, weights, bias):
    
    print("\n---------Neuron Calculation Starts---------")

    # Display inputs and weights 
    print("Inputs (x):", inputs)
    print("Weights (w):", weights)
    print("Bias (b):", bias)

    # ---------------------------------------------------
    # Step 2.1 - Weighted Sum Calculation 
    # Formula: z = (x1.w1 + x2.w2 + .... + xn*wn) + bias
    # ---------------------------------------------------

    z = sum(w * x for w, x in zip(weights, inputs)) + bias 

    print("\nStep 1 - Weighted Sum Calculation")
    print("z = w.x + b =", z)

    # ---------------------------------------------------
    # Step 2.2 - Activation Function 
    # ---------------------------------------------------

    y_hat = relu(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function : ReLU")
    print("Output (y_hat) =", y_hat)

    print("\n------- Neuron Calculation End -------")

    return z, y_hat


# ---------------------------------------------------
# Step 3 -Plot relu finction 
# ---------------------------------------------------
# this helps to visualize how ReLU behaves 

def plot_relu():
    
    # Generate range of values for z 
    z_values = np.linspace(-10, 10, 200)

    # Apply ReLU on all values 
    relu_values = np.maximum(0, z_values)

    # plot graph 
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, relu_values, label="ReLU Function", linewidth=2, color="green")

    # Axes lines 
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")

    # Labels and title 
    plt.title("ReLU Activation Function", fontsize=0.5)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    # Grid and legend 
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # show graph
    plt.show()

# ---------------------------------------------------
# Step 4 - Main Function 
# ---------------------------------------------------

def main():
    
    print("\n===================== Neuron Demo ========================\n")

    # Example Inputs (features) 
    inputs = [1.0, 2.0, 3.0]

    # Corresponding Weights 
    weights = [0.6, 0.4, -0.2]

    # Bias value 
    bias = 0.5 

    # Perform forward propagation 
    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)

    # Plot ReLU Graph 
    plot_relu()

# ---------------------------------------------------
# Starter 
# ---------------------------------------------------


if __name__ == "__main__":
    main()

