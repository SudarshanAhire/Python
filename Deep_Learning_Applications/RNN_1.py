import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

# Sample : Sequence classification 
# Suppose we have 10 sequences, each with 5 timesteps, vocabulary size = 20
X = np.random.randint(20, size=(10, 5))  # Input sequences (10 samples, 5 timestamp)

y = np.random.randint(2, size=(10, 1))  # Binary output (labels)

# Build RNN model 
model = Sequential()

# Word Embedding
model.add(Embedding(input_dim=20, output_dim=8, input_length=5))

# RNN layer 
model.add(SimpleRNN(16, activation='tanh'))

# Output Layer 
model.add(Dense(1, activation='sigmoid'))

# Complete Model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train 
model.fit(X, y, epochs=5, verbose=1)

# Prediction
print("Sample Prediction :", model.predict(X[:1]))