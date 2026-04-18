#------------------------------------------------------
# Network Structure:
# Input Layer : 2 inputs 
# Hidden Layer : 2 Neurons with ReLU activation 
# Output Layer : 1 neuron with sigmoid activation 
# 
# purpose :
# To understand how data moves from input layer 
# to hidden layer and finally to output layer 
#------------------------------------------------------

import math 

#------------------------------------------------------
# Function Name : Marvellous_ReLU
# Description : Applies ReLU activation function 
# Formula : ReLU(x) = max(0, x)
# Use : Commonly used in hidden layers 
#------------------------------------------------------

def Marvellous_ReLU(value):
    return max(0, value)

#------------------------------------------------------
# Function Name : Marvellous_Sigmoid
# Description : Applies Sigmoid activation function 
# Formula : 1 / (1 + e^(-x))
# Use : Commaonly used in output layer for binary classfication 
# Output range : 0 to 1 
#------------------------------------------------------

def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))

#------------------------------------------------------
# Function Name : Marvellous_Calculate_Weighted_Sum 
# Description : Calculates weighted sum of inputs 
# Formula : z = (x1.w1 + x2.w2 + ..... + xn.wn) + b
# Parameters :
# inputs -> List of input values 
# weights -> List of weights 
# bias -> Bias Value 
# Return : weighted sum 
#------------------------------------------------------

def Marvellous_Calculate_Weighted_Sum(inputs, weights, bias):
    weighted_sum = sum(weight * input for weight, input in zip(weights, inputs)) + bias
    return weighted_sum

#------------------------------------------------------
# Function Name : Marvellous_Display_Multiplication_Details 
# Description : Display step-by-step multiplication of 
#               inputs and weights for one neuron
# Parameters :
# inputs -> List of inputs 
# weights -> List of weights 
#------------------------------------------------------

def Marvellous_Display_Multiplication_Details(inputs, weights):
    print("Step 1 : Multiply inputs by corresponding weights")
    for index in range(len(inputs)):
        print(f"({weights[index]} * {inputs[index]}) = {weights[index] * inputs[index]:.3f}")

#------------------------------------------------------
# Function Name : Marvellous_Process_Hidden_Layer 
# Description : Processes all neurons of hidden layer 
#                using ReLU activation function 
# Parameters :
# inputs -> Input values from input layer
# hidden_weights -> Weights matrix for hidden layer
# Hidden_biases -> bias list for hidden neurons 
# Returns : List of hidden layer outputs
#------------------------------------------------------

def Marvellous_Process_Hidden_Layer(inputs, hidden_weights, hidden_biases):
    hidden_outputs = []

    print("\n==================== HIDDEN LAYER ========================")

    for neuron_index in range(len(hidden_weights)):
        print(f"Hidden Neuron {neuron_index + 1}:")

        current_weights = hidden_weights[neuron_index]
        current_bias = hidden_biases[neuron_index]

        # Display multiplication details 
        Marvellous_Display_Multiplication_Details(inputs, current_weights)

        # Calculate Weighted sum 
        z_value = Marvellous_Calculate_Weighted_Sum(inputs, current_weights, current_bias)
        print(f"Step 2 : Add all multiplication results and bias {current_bias}")
        print(f"z = {z_value:.3f}")

        # Apply ReLU Activation 
        activated_output = Marvellous_ReLU(z_value)
        print(f"Step 3 : Apply ReLU Activation")
        print(f"ReLU ({z_value:.3f}) = {activated_output:.3f}\n")

        hidden_outputs.append(activated_output)

    return hidden_outputs

#------------------------------------------------------
# Function Name : Marvellous_Process_Output_Layer
# Description : Processes output layer neuron using
#               sigmoid activation function
# Parameters :
# hidden_outputs -> Outputs from hidden layer 
# output_weights -> Weights of output neuron 
# output_bias -> Bias of output neuron 
# Return : Final weighted sum and final output 
#------------------------------------------------------

def Marvelllous_Process_Output_Layer(hidden_outputs, output_weights, output_bias):
    print("Output Neuron:")
    print("Step 1 : Multiply hidden layer outputs by output weights")

    for index in range(len(hidden_outputs)):
        print(
            f"({output_weights[index]} * {hidden_outputs[index]:.3f}) = {output_weights[index] * hidden_outputs[index]:.3f}"
        )

    # Calculate weighted sum for all output layers 
    z_output = Marvellous_Calculate_Weighted_Sum(hidden_outputs, output_weights, output_bias)
    print(f"Step 2 - Add all multiplication results and bias {output_bias}")
    print(f"z = {z_output:.3f}")

    # Apply sigmoid function 
    final_output = Marvellous_Sigmoid(z_output)
    print("Step 3 - Apply Sigmoid activation")
    print(f"Sigmoid({z_output:.3f}) = {final_output:.3f}")

    return z_output, final_output

def Marvellous_Display_Network_Summuary(hidden_outputs, final_output):
    print("\n=============== Final Summuary ===================")
    print(f"Hidden Layer Outputs :{hidden_outputs}")
    print(f"Final network output : {final_output:.3f}")
    print(f"Confidence Percentage : {final_output * 100:.2f}%")

    if final_output >= 0.5:
        print("Prediction : Positive Class")
    else:
        print("prediction : Negative Class")

def Marvellous_ANN_Forward_Pass(inputs):
    print("\n==================== Input Layer ======================")
    print(f"Input x1 = {inputs[0]}")
    print(f"Input x2 = {inputs[1]}")

    hidden_weights = [
        [0.5, -0.2],      # Weights for hidden neuron 1
        [0.8, 0.4]        # Weights for hidden neuron 2
    ]

    hidden_biases = [
        0.1,  # Bias for hidden neuron 1
        -0.1  # Bias for hidden neuron 2
    ]

    output_weights = [1.0, -1.5]
    output_bias = 0.2

    # process hidden layer 
    hidden_outputs = Marvellous_Process_Hidden_Layer(
        inputs,
        hidden_weights,
        hidden_biases
    )

    # Process output layer 
    z_output, final_output = Marvelllous_Process_Output_Layer(
        hidden_outputs,
        output_weights,
        output_bias
    )

    # Display Summary 
    Marvellous_Display_Network_Summuary(hidden_outputs, final_output)

def main():
    inputs = [2.0, 3.0]

    Marvellous_ANN_Forward_Pass(inputs)

if __name__ == "__main__":
    main()