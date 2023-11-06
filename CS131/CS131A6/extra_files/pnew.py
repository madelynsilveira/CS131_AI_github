import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

# # layer object
class Layer_Dense:
    def __init__(self, input_size, output_size):
        self.weights = 0.1 * np.random.randn(input_size, output_size) # shape = inputs by neurons
        self.bias = np.zeros((1, output_size))
        # self.bias = np.random.randn(output_size, 1)
    def forward(self, inputs):
        # self.inputs = inputs
        #return np.dot(self.weights, self.inputs) + self.bias

        self.output = np.dot(inputs, self.weights) + self.bias

    def backward(self, output_gradient, learning_rate): # applying simple gradient descent
        weights_gradient = np.dot(output_gradient, self.inputs.T)
        self.weights -= learning_rate * weights_gradient
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T, output_gradient)
        # self.output = np.dot(self.weights.T, output_gradient)

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

# vid 2 Activation layer
class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime
    def forward(self, inputs):
        self.inputs = inputs
        return self.activation(self.inputs)
    def backward(self, output_gradient, learning_rate):
        return np.multiply(output_gradient, self.activation_prime(self.input))

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

# now we need to calculate accuracy = mean of equivalence check
