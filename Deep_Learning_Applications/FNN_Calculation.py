import math

def relu(x):
    return max(0.0, x)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

x = [2.0, 3.0]

w1 = [[0.5, -0.2],
      [0.8, 0.4]]
b1 = [0.1, -0.1]

# Hidden Layer 
z1 = w1[0][0]*x[0] + w1[0][1]*x[1] + b1[0]
a1 = relu(z1)

z2 = w1[1][0]*x[0] + w1[1][1]*x[1] + b1[1]
a2 = relu(z2)

# Output Layer 
w2 = [1.2, -0.7]
b2 = 0.05

z_out = w2[0]*a1 + w2[1]*a2 + b2
yhat = sigmoid(z_out)

print(yhat)   # 0.22443598573092652