import tensorflow as tf

# Define matrices

A = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
B = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

matmul = tf.matmul(A, B)     # Matrix Multiplication 
transpose = tf.transpose(A)  # Transpose

print("Matrix A:\n", A.numpy())
print("Matrix B:\n", B.numpy())
print("A * B:\n", matmul.numpy())
print("Tranpose of A:\n", transpose.numpy())
