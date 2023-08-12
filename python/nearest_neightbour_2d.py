from math import sqrt


class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.value)


compare_x = lambda value: value[0]
compare_y = lambda value: value[1]



def build_balanced_kd_tree(values, coordinate: bool = 1):

	if not values:
		return None


	values.sort(key = compare_x if coordinate else compare_y)
	values_len = len(values)
	mid = values_len//2
	head = Node(values[mid])

	head.left = build_balanced_kd_tree(values[:mid], (coordinate+1)%2)
	head.right = build_balanced_kd_tree(values[mid+1:], (coordinate+1)%2)

	return head


def store_bin_tree(head):

	nodes= [head]

	current = 0

	while current<len(nodes):

		if nodes[current]:
			nodes.append(nodes[current].left)
			nodes.append(nodes[current].right)

		current+=1

	while nodes and nodes[-1] == None:
		nodes.pop()

	return nodes

#first take

# def find_nearest_neighbour(tree, point):
# 	path = [tree]

# 	coordinates_num = 2

# 	def calc_dist(point1, point2):
# 		return sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2)

# 	def explore(path,point, coordinates_num):

# 		coordinate = (len(path)-1) % coordinates_num

# 		while path[-1]:
# 			if point[coordinate] < path[-1].value[coordinate]:
# 				path.append(path[-1].left)
# 			else:
# 				path.append(path[-1].right)

# 			coordinate+=1
# 			coordinate%=coordinates_num

# 		path.pop()

# 	explore(path,point, coordinates_num)

# 	if path[-2]:

# 		coordinate = (len(path)-1) % coordinates_num

# 		x = point[:]
# 		x[coordinate] = path[-2].value[coordinate]

# 		while calc_dist(point, x) <= calc_dist(point, path[-1].value):
# 			print(path, coordinate, calc_dist(point, x))
# 			path[-1] = path[-2].left if path[-1] == path[-2].right else path[-2].right
# 			explore(path,point, coordinates_num)

# 			coordinate = (len(path)-1) % coordinates_num

# 			x = point[:]
# 			x[coordinate] = path[-2].value[coordinate]




# 	return path[-1].value


def get_closest_node(target, node1, node2):
	return node1 if (node1.value[0] - target[0])**2 + (node1.value[1] - target[1])**2 < (node2.value[0] - target[0])**2 + (node2.value[1] - target[1])**2 else node2



def find_nearest_neighbour(root, target, depth = 0, k=2):

	if root == None:
		return None

	next_branch = None
	other_branch = None

	if target[depth%k] < root.value[depth%k]:
		next_branch = root.left
		other_branch = root.right
	else:
		next_branch = root.right
		other_branch = root.left

	temp = find_nearest_neighbour(next_branch, target, depth+1, k)

	best = root if not temp else get_closest_node(target, temp, root)

	if (best.value[0] - target[0])**2 + (best.value[1] - target[1])**2 >= target[depth%k]- root.value[depth%k]:
		temp = find_nearest_neighbour(other_branch, target, depth+1, k)
		best = best if not temp else get_closest_node(target,temp,best)


	return best




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

	tree_of_points = build_balanced_kd_tree(points)

	print(find_nearest_neighbour(tree_of_points, [2,3]))


