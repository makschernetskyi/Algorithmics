import numpy as np
from math import e, tanh, cosh, atanh, ceil
from alive_progress import alive_bar

class DNN:
	def __init__(self, hidden_layers = 0, activation_function = "relu"):
		self.activation_function_name = activation_function
		if hidden_layers:
			self.hidden_layers_shapes = np.array([0]*hidden_layers)

		if activation_function == "relu":
			self.activation_function = np.vectorize(DNN.ReLU)
		elif activation_function == "sigmoid":
			self.activation_function = np.vectorize(DNN.sigmoid)
		elif activation_function == "tanh":
			self.activation_function = np.vectorize(DNN.tanh)
		else:
			raise Exception("invalid activation_function parameter")

	def ReLU(x):
		return float(max(0,x))

	def sigmoid(x):
		return float(1/(1+e**(-x)))

	def tanh(x):
		return float(tanh(x))

	def set_input_layer(self, shape):
		self.input_shape = shape

	def set_output_layer(self, shape):
		self.output_shape = shape

	def set_hidden_layers(self, shapes):
		if hasattr(self,'hidden_layers_shapes'):
			self.hidden_layers_shapes = shapes

	def construct_weights_and_biases(self):
		if hasattr(self,'hidden_layers_shapes'):
			self.weights = [np.random.rand(self.input_shape, self.hidden_layers_shapes[0])]
			for i in range(len(self.hidden_layers_shapes)-1):
				self.weights.append(np.random.rand(self.hidden_layers_shapes[i], self.hidden_layers_shapes[i+1]))
			self.weights.append(np.random.rand(self.hidden_layers_shapes[-1], self.output_shape))

			self.biases = list(map(lambda shape: np.random.rand(shape),self.hidden_layers_shapes)) + [np.random.rand(self.output_shape)]
		else:
			self.weights = [np.random.rand(self.input_shape, self.output_shape)]
			self.biases = [np.random.rand(self.output_shape)]

	def import_weights(self, weights):
		self.weights = weights
	def import_biases(self, biases):
		self.biases = biases



	def feed_forward(self,X):

		if X.shape != (self.input_shape,):
			raise Exception(f"input shape is not ({self.input_shape},)")

		if hasattr(self,'hidden_layers_shapes'):
			last_layer_res = X
			for i in range(len(self.hidden_layers_shapes)):
				last_layer_res = self.activation_function(last_layer_res.dot(self.weights[i])+self.biases[i])
			output = self.activation_function(last_layer_res.dot(self.weights[-1]) + self.biases[-1])
			return output

		return self.activation_function(np.dot(X, self.weights[0]))

	def pass_forward(self, X):

		if X.shape != (self.input_shape,):
			raise Exception(f"input shape is not ({self.input_shape},)")

		layer_outputs = [X]

		if hasattr(self,'hidden_layers_shapes'):
			for i in range(len(self.hidden_layers_shapes)):
				layer_outputs.append(self.activation_function(layer_outputs[-1].dot(self.weights[i])+self.biases[i]))
			layer_outputs.append(self.activation_function(layer_outputs[-1].dot(self.weights[-1]) + self.biases[-1]))
			return layer_outputs

		layer_outputs.append(self.activation_function(np.dot(X, self.weights[0])))
		return layer_outputs

	def get_activation_to_derivative_function(activation_function):
		if activation_function == "relu":
			return lambda x: int(x>0)
		if activation_function == "sigmoid":
			return lambda x: x*(1-x)
		if activation_function == "tanh":
			return lambda x: 1/cosh(atanh(x))

		raise Exception("invalid activation_function parameter")

	def pass_backward(self, layer_outputs, expected):
		gradients = []
		get_derivative_from_activation = DNN.get_activation_to_derivative_function(self.activation_function_name)
		cost_gradient = np.zeros_like(layer_outputs[-1])
		for i in range(len(layer_outputs[-1])):
			cost_gradient[i] = 2*(layer_outputs[-1][i]-expected[i])
		gradients.append(cost_gradient)

		for i in range(len(layer_outputs)-2,-1, -1):
			gradient = np.zeros_like(layer_outputs[i], dtype=float)
			for k in range(len(layer_outputs[i])):
				for j in range(len(layer_outputs[i+1])):
					gradient[k] += gradients[-1][j]*get_derivative_from_activation(layer_outputs[i+1][j])*self.weights[i][k][j]
			gradients.append(gradient)

		return list(reversed(gradients))

	def get_weights_gradients(self, activations_gradients, layer_outputs):
		weights_gradients = []

		get_derivative_from_activation = DNN.get_activation_to_derivative_function(self.activation_function_name)

		for i in range(len(layer_outputs)-1):
			gradient = np.zeros_like(self.weights[i])
			for k in range(len(layer_outputs[i])):
				for j in range(len(layer_outputs[i+1])):
					weight_derivative = activations_gradients[i+1][j]*get_derivative_from_activation(layer_outputs[i+1][j])*layer_outputs[i][k]
					gradient[k][j] = weight_derivative
			weights_gradients.append(gradient)

		return weights_gradients

	def get_biases_gradients(self, activations_gradients, layer_outputs):
		biases_gradients = []

		get_derivative_from_activation = DNN.get_activation_to_derivative_function(self.activation_function_name)

		for i in range(len(self.biases)):
			gradient = np.zeros_like(self.biases[i])
			for j in range(self.biases[i].shape[0]):
				bias_derivative = activations_gradients[i+1][j]*get_derivative_from_activation(layer_outputs[i+1][j])
				gradient[j] = bias_derivative
			biases_gradients.append(gradient)

		return biases_gradients

	def propagate_backwards(self, inputs, expected_outputs):

		number_of_inputs = len(inputs)

		averaged_weights_gradients = [np.zeros_like(w) for w in self.weights]
		averaged_biases_gradients = [np.zeros_like(b) for b in self.biases]


		for X,Y in zip(inputs, expected_outputs):

			layer_outputs = self.pass_forward(X)
			activations_gradients = self.pass_backward(layer_outputs,Y)

			weights_gradients = self.get_weights_gradients(activations_gradients, layer_outputs)
			biases_gradients = self.get_biases_gradients(activations_gradients, layer_outputs)

			for i in range(len(self.weights)):
				for j in range(self.weights[i].shape[0]):
					for k in range(self.weights[i].shape[1]):
						averaged_weights_gradients[i][j][k] += weights_gradients[i][j][k]

			for i in range(len(self.biases)):
				for j in range(self.biases[i].shape[0]):
					averaged_biases_gradients [i][j] += biases_gradients[i][j]

		for i in range(len(self.weights)):
				for j in range(self.weights[i].shape[0]):
					for k in range(self.weights[i].shape[1]):
						averaged_weights_gradients[i][j][k] /= number_of_inputs

		for i in range(len(self.biases)):
			for j in range(self.biases[i].shape[0]):
				averaged_biases_gradients [i][j] /= number_of_inputs

		return averaged_weights_gradients, averaged_biases_gradients

	def update_weights_and_biases(self, weights_gradients, biases_gradients, learning_rate=1):

		for i in range(len(self.weights)):
			for j in range(self.weights[i].shape[0]):
				for k in range(self.weights[i].shape[1]):
					self.weights[i][j][k] -= learning_rate*weights_gradients[i][j][k]

		for i in range(len(self.biases)):
			for j in range(self.biases[i].shape[0]):
				self.biases[i][j] -= learning_rate*biases_gradients[i][j]

	def batch_generator(data, labels, batch_size):
		data_len = len(data)
		for i in range(0, data_len, batch_size):
			yield data[i : i + batch_size], labels[i : i + batch_size]

	def learn(self, inputs, labels, batch_size, epochs=1, shuffle=False):

		batches_num = ceil(len(inputs)/batch_size)

		print("Starting training the model...")
		for i in range(epochs):
			print(f"epoch: {i}")
			X,Y = inputs, labels
			if shuffle:
				temp = list(zip(X, Y))
				np.random.shuffle(temp)
				X,Y = [list(t) for t in zip(*temp)]


			batch_gen = DNN.batch_generator(X,Y,batch_size)
			with alive_bar(batches_num, bar="filling") as bar:
				for x, y in batch_gen:
					weights_gradients, biases_gradients = self.propagate_backwards(x,y)
					self.update_weights_and_biases(weights_gradients, biases_gradients)
					bar()
		print("Done! The model was trained!")





if __name__ == '__main__':
	dnn = DNN(1, "relu")
	dnn.set_input_layer(2)
	dnn.set_output_layer(1)
	dnn.set_hidden_layers([1])
	dnn.import_weights([np.array([[1.5],[2.0]]), np.array([[0.7]])])
	dnn.import_biases([np.array([1]), np.array([1])])

	X = np.array([
		[1,2], [8,5], [12,2], [25,5],
	])

	Y = np.array([
		[4], [1], [4], [9],
	])

	dnn.learn(X, Y, batch_size=1 ,epochs=10, shuffle=True)