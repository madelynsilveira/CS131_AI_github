# training for error = how close was it to getting each one right
# categorical cross-entropy

import math
# import numpy as np

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0] # one-hot coding

# we want to calculate the loos from this
loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

loss = -math.log(softmax_output[0]) # measurement of error
print(loss)

# import nnfs

# # sofmax activation function
# nnfs.init()

# layer_outputs = [[4.8, 1.21, 2.385],
#                 [8.9, -1.81, 0.2],
#                 [1.41, 1.051, 0.026]]

# exp_values = np.exp(layer_outputs)
# norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

# print(norm_values)


# # training a model --> how wrong is this model?
# layer_outputs = [4.8, 1.21, 2.385]

# E = math.e #2.718

# exp_values = np.exp(layer_outputs)

# # for output in layer_outputs:
# #     exp_values.append(E**output)

# # normalization after exponentiation
# norm_values = exp_values / np.sum(exp_values)
# # norm_base = sum(exp_values)
# # norm_values = []

# # for value in exp_values:
# #     norm_values.append(value / norm_base)

# print(exp_values)
# print(norm_values)
# print(sum(norm_values))