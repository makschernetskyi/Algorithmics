import random
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def get_distance(point1, point2):
	coordinates = len(point1)
	distance = 0
	for i in range(coordinates):
		distance += (point1[i]-point2[i])*(point1[i]-point2[i])
	return sqrt(distance)

def find_nearest_to_target(target, points):
	index = 0
	nearest_point = points[index]
	distance = get_distance(target, points[index])
	for i, point in enumerate(points):
		dist_to_point = get_distance(target, point)
		if dist_to_point<distance:
			nearest_point = point
			distance = dist_to_point
			index = i
	return [nearest_point, index]




def k_means(data, k):


	if data == []:
		return []

	features = len(data[0])
	centroids = random.sample(data, k)



	clusters = [[] for c in centroids]

	next_cycle = True


	while next_cycle:
		new_clusters = [[] for c in centroids]
		for point in data:
			new_clusters[find_nearest_to_target(point, centroids)[1]].append(point)



		new_centroids = []
		for cluster in new_clusters:
			cluster_len = len(cluster)
			sum_by_features = [0]*features
			for point in cluster:
				for i in range(features):
					sum_by_features[i] += point[i]

			if cluster_len:
				new_centroids.append([sum_by_feature/cluster_len for sum_by_feature in sum_by_features])

		clusters = new_clusters
		if new_centroids == centroids:
			next_cycle = False
		else:
			centroids = new_centroids






	return clusters

def calculate_square_error(clusters):
	features = len(clusters[0][0])
	SSE = 0
	for cluster in clusters:
		cluster_len = len(cluster)
		sum_by_features = [0]*features
		for point in cluster:
			for i in range(features):
				sum_by_features[i] += point[i]
			centroid = [sum_by_feature/cluster_len for sum_by_feature in sum_by_features]


		for point in cluster:
			SSE += get_distance(centroid, point)**2

	return SSE





if __name__ == '__main__':

	points = [
		[1,1],
		[3,1],
		[1,2],
		[3,3],
		[-1,3],
		[-2,1],
		[-3,1],
		[-1,-1],
		[-2,-3],
		[-4,-4]
	]

	points_2 = [
		[2, 5], [3, 4], [2, 6], [4, 5], [3, 5],
		[10, 12], [11, 11], [9, 13], [10, 11], [11, 12],
		[20, 25], [21, 24], [22, 23], [19, 26], [23, 25],
		[30, 35], [32, 34], [31, 33], [29, 36], [30, 34]
	]

	testpoints = [
		[1,1],
		[1,2],
		[2,1],

		[-1,-1],
		[-1,-2],
		[-2,-1],

		[1,-1],
		[1,-2],
		[2,-1]
	]

	k_list = list(range(1,len(points_2)))
	SSE_list = []

	for k in k_list:
		clustered_data = k_means(points_2,k)
		SSE_list.append(calculate_square_error(clustered_data))


	plt.scatter(k_list, SSE_list)
	plt.xlabel('K')
	plt.ylabel('SSE')
	plt.show()




	clustered_data = k_means(points_2,4)
	# print(f"SSE = {calculate_square_error(clustered_data)}",'\n\n', clustered_data)