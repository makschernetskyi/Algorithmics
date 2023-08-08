from typing import List
import numpy as np
import matplotlib.pyplot as plt





def costFunction(features: List[float], labels: List[float], predict_func, a, k) -> float:
	errors_sum = 0
	total = len(features)
	for i in range(0, total):
		errors_sum+=(predict_func(features[i], a, k) - labels[i])**2
	return errors_sum/(2*total)


def objective_function(feature: float, a:float, k:float):
	return feature*a+k


def gradient_descent(features, labels, step_const):
	def cost_function_gradient(features, labels, a, k):
		errors_sum_resp_a = 0
		total = len(features)
		for i in range(0, total):
			errors_sum_resp_a+=features[i]*(a*features[i] + k - labels[i])
		errors_sum_resp_k = 0
		for i in range(0, total):
			errors_sum_resp_k+=(a*features[i] + k - labels[i])
		return [errors_sum_resp_a/total, errors_sum_resp_k/total]

	a = 0
	k = 0
	accuracy = 0.00001
	gradient = [1,1]
	while max(abs(gradient[0]),abs(gradient[1]))>accuracy:
		gradient = cost_function_gradient(features, labels, a, k)
		a-=step_const*gradient[0]
		k-=step_const*gradient[1]
	return [a,k]






def main():

	features = np.array([0,0.5,1,2,3])
	labels = np.array([-1.25,-0.9,-0.75, -0.5, -0.5])

	coefficients = gradient_descent(features, labels, 0.01)

	predicted = np.array(list(map(lambda x: objective_function(x, coefficients[0], coefficients[1]),features)))

	plt.figure(figsize=(15, 8))
	plt.scatter(features, labels)
	plt.plot(features, predicted)
	plt.title(f"cost: {costFunction(features,labels,objective_function,coefficients[0], coefficients[1])}")
	plt.show()


if __name__ == '__main__':
	main()