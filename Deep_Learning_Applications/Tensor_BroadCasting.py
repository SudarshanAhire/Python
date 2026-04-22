import tensorflow as tf

C = tf.constant([1, 2, 3], dtype=tf.float32)
D = tf.constant(2.0)

broadcast_add = C + D
broadcast_mul = C * D 

print("C:", C.numpy())
print("C + D:", broadcast_add.numpy())
print("C * D:", broadcast_mul.numpy())
