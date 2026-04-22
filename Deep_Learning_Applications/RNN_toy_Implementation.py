import numpy as np

# Example sentence : "i Love AI" (encoded as numbers)
sequence = [1, 2, 3] # Let's say 1=I, 2=Love, 3=AI

# Initialization weights and hidden state 
Wx, Wh, b = 0.5, 0.8, 0.1   # Random chosen values
h = 0   # initial hidden state

print("Processing sequence step by step:")

for t, x in enumerate(sequence):
    h = np.tanh(Wx * x + Wh * h + b)  # memory update
    print(F"Timestep {t+1} | Input={x} | Hidden State={h:.4f}")
