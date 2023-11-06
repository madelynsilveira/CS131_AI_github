import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

# # layer object
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) # shape = inputs by neurons
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# rectified linear object
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

# Softmax activation object
class Activation_Softmax:
    def forward(self, inputs):
        # exponential values of a batchwise (subtracting max to prevent overflow)
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True)) 
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities # outputs probability distribution for each class for each sample (adds to 1)

# Common Loss class
class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses) # batch loss
        return data_loss

# Categorical cross-entropy object
class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) # catch for log of 0 probability
        # find out what kind of values (scalar of one-hot encoded) they have passed
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2: # one hot encoded
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods


X, y = spiral_data(samples=100, classes=3)

# print(X, y)
dense1 = Layer_Dense(2, 3) # (input, output)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

# now we need to train this model: how right and how wrong? --> loss function
loss_function = Loss_CategoricalCrossentropy()
loss = loss_function.calculate(activation2.output, y)

print(loss)

# now we need to calculate accuracy = mean of equivalence check





# layer1 = Layer_Dense(2, 5)
# activation1 = Activation_ReLU()

# layer1.forward(X)
# activation1.forward(layer1.output)
# print(activation1.output)


# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
# output = []

# for i in inputs:
#         output.append(max(i, 0))

# print(output)





# three neurons with four inputs
# 5.1,3.5,1.4,0.2,Iris-setosa

# inputs = outputs of previous neurons
# inputs = [[1, 2, 3, 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5, 2.7, 3.3, -0.8],]

# weights1 = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87],]
# biases1 = [2, 3, 0.5] 

# weights2 = [[0.1, -0.14, 0.5],
#            [-0.5, 0.12, -0.33],
#            [-0.44, 0.73, -0.13],]
# biases2 = [-1, 2, -0.5] 

# # use dot product to multiply each input by its weight
# # then add dot product vector to biases vector to add respective biases
# # transpose to make the shapes work
# layer1_outputs = np.dot(inputs, np.array(weights1).T) + biases1
# layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

# print(layer2_outputs)