import numpy as np
import math


class LayerDense:
    def __init__(self, n_inputs, n_neurons, sigma_weights, sigma_biases):
        self.outputs = None
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        rng = np.random.default_rng()
        self.weights = np.array(sigma_weights * rng.standard_normal(size=(n_inputs, n_neurons)))
        self.biases = np.array(sigma_biases * rng.standard_normal(size=(1, n_neurons)))

    def forward(self, inputs):
        if not len(inputs) == self.n_inputs:
            raise ValueError("network layer got wrong number of inputs")
        self.outputs = np.squeeze(np.dot(inputs, self.weights) + self.biases)

        print(self.outputs.shape)

    def show_weights(self):
        print(self.weights.shape)
        print(self.weights)

    def show_biases(self):
        print(self.biases.shape)
        print(self.biases)


class NeuralNetwork:
    def __init__(self, shape, sigma_weights=0.1, sigma_biases=0.1):
        self.outputs = None
        self.shape = shape
        self.network = []
        for i, layer_size in enumerate(shape):
            if i == 0:
                continue
            self.network.append(LayerDense(shape[i-1], shape[i], sigma_weights, sigma_biases))

    def calculate(self, inputs):
        temp = None
        for layer in self.network:
            if layer == self.network[0]:
                layer.forward(inputs)
            else:
                layer.forward(temp)
            temp = layer.outputs
        self.outputs = temp

    def print_network(self):
        for i, x in enumerate(self.network):
            print(f"Layer {i+1}:")
            x.show_weights()
            x.show_biases()


if __name__ == "__main__":
    network = NeuralNetwork([4, 2, 3, 2, 2])
    network.print_network()
    network.calculate([1, 2, 3, 4])
    print(network.outputs)
